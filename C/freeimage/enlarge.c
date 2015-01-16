/*
   use libfreeimage to enlarge a bitmap by copying each line twice

   $ gcc -o enlarge enlarge.c -lfreeimage
*/

#include <stdio.h>
#include <stdlib.h>
#include "FreeImage.h"

#define TEST_FILE   "inp.bmp"
#define OUT_FILE    "out.bmp"

unsigned g_bpp;
unsigned g_width;
unsigned g_height;
unsigned g_pitch;

void enlarge_image(FIBITMAP* bid);

int main()
{
    FIBITMAP* bitmap;

    // load image
    //bitmap = FreeImage_Load(FIF_JPEG, TEST_FILE, JPEG_DEFAULT);
    bitmap = FreeImage_Load(FIF_BMP, TEST_FILE, BMP_DEFAULT);
    if (!bitmap)
    {
        printf("cannot load image: %s\n", TEST_FILE);
        exit(-1);
    }

    printf("used_color = %d\n", FreeImage_GetColorsUsed(bitmap));
    g_bpp = FreeImage_GetBPP(bitmap);
    printf("bpp = %d\n", g_bpp);
    printf("bits = %p\n", FreeImage_GetBits(bitmap));
    g_width = FreeImage_GetWidth(bitmap);
    printf("width = %d\n", g_width);
    g_height = FreeImage_GetHeight(bitmap);
    printf("height = %d\n", g_height);
    g_pitch = FreeImage_GetPitch(bitmap);
    printf("pitch = %d\n", g_pitch);

    enlarge_image(bitmap);

    // unload image
    if (bitmap)
        FreeImage_Unload(bitmap);

    return 0;
}

void enlarge_image(FIBITMAP* dib)
{
    // this code assumes there is a bitmap loaded and
    // present in a variable called 'dib'
    unsigned width = FreeImage_GetWidth(dib);
    unsigned height = FreeImage_GetHeight(dib);
    unsigned pitch = FreeImage_GetPitch(dib);
    FREE_IMAGE_TYPE image_type = FreeImage_GetImageType(dib);
    unsigned x, y;

    // test pixel access avoiding scanline calculations
    // to speed-up the image processing
    if (image_type == FIT_RGBF)
    {
        BYTE *bits = (BYTE*)FreeImage_GetBits(dib);
        for(y = 0; y < height; y++)
        {
            FIRGBF *pixel = (FIRGBF*)bits;
            for(x = 0; x < width; x++)
            {
                pixel[x].red = 128;
                pixel[x].green = 128;
                pixel[x].blue = 128;
            }
            // next line
            bits += pitch;
        }
    }
    else if ((image_type == FIT_BITMAP) && (FreeImage_GetBPP(dib) == 24))
    {
        BYTE *bits = (BYTE*)FreeImage_GetBits(dib);
        BYTE *out_bits;
        FIBITMAP *out_dib = NULL;
        unsigned iterx, itery;
        unsigned out_pitch;

        out_dib = FreeImage_Allocate(g_width*2,g_height*2,24,0,0,0);
        if (out_dib == NULL)
        {
            printf("cannot allocate new dib, exit...\n");
            return;
        }
        out_pitch = FreeImage_GetPitch(out_dib);

        out_bits = (BYTE*)FreeImage_GetBits(out_dib);
        for (y = 0; y < height; y++)
        {
            BYTE *pixel = (BYTE*)bits;
            BYTE *out_pix = (BYTE*)out_bits;

            for (itery = 0; itery < 2; ++itery)
            {
                for(x = 0; x < width; x++)
                {
                    for (iterx = 0; iterx < 2; ++iterx)
                    {
                        out_pix[FI_RGBA_RED] = pixel[FI_RGBA_RED];
                        out_pix[FI_RGBA_GREEN] = pixel[FI_RGBA_GREEN];
                        out_pix[FI_RGBA_BLUE] = pixel[FI_RGBA_BLUE];
                        out_pix += 3;
                    }
                    pixel += 3;
                }
                // next line
                out_bits += out_pitch;
            }
            // next line
            bits += pitch;
        }
        if (! FreeImage_Save(FIF_BMP, out_dib, OUT_FILE, 0))
        {
            printf("save image failed\n");
        }
    }
}
