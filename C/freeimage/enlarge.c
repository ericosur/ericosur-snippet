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

void show_image_info(FIBITMAP* bitmap)
{
    printf("used_color = %d\n", FreeImage_GetColorsUsed(bitmap));
    g_bpp = FreeImage_GetBPP(bitmap);
    printf("bpp = %d\n", g_bpp);
    printf("bits = %p\n", FreeImage_GetBits(bitmap));
    g_width = FreeImage_GetWidth(bitmap);
    printf("width = %d\n", g_width);
    g_height = FreeImage_GetHeight(bitmap);
    printf("height = %d\n", g_height);
    printf("memory size: %u\n", FreeImage_GetMemorySize(bitmap));
    g_pitch = FreeImage_GetPitch(bitmap);
    printf("pitch = %d\n", g_pitch);
}

void enlarge_image(const char* ofn, FIBITMAP* dib)
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
        if (! FreeImage_Save(FIF_BMP, out_dib, ofn, 0))
        {
            printf("save image failed\n");
        }
    }
}

/** Generic image loader
@param lpszPathName Pointer to the full file name
@param flag Optional load flag constant
@return Returns the loaded dib if successful, returns NULL otherwise
*/
FIBITMAP* load_generic(const char* fn, int flag)
{
    FREE_IMAGE_FORMAT fif = FIF_UNKNOWN;
    // check the file signature and deduce its format
    // (the second argument is currently not used by FreeImage)
    fif = FreeImage_GetFileType(fn, 0);
    if(fif == FIF_UNKNOWN) {
        // no signature ?
        // try to guess the file format from the file extension
        fif = FreeImage_GetFIFFromFilename(fn);
    }
    printf("%s: %s\n", fn, FreeImage_GetFormatFromFIF(fif));
    // check that the plugin has reading capabilities ...
    if((fif != FIF_UNKNOWN) && FreeImage_FIFSupportsReading(fif)) {
        // ok, let's load the file
        FIBITMAP *dib = FreeImage_Load(fif, fn, flag);
        // unless a bad file format, we are done !
        return dib;
    }
    return NULL;
}

int main(int argc, char** argv)
{
    FIBITMAP* bitmap;

    if (argc == 1) {
        bitmap = load_generic(TEST_FILE, BMP_DEFAULT);
    } else {
        bitmap = load_generic(argv[1], BMP_DEFAULT);
    }
    if (bitmap == NULL)  {
        printf("failed to load...\n");
        exit(-1);
    }
    show_image_info(bitmap);
    printf("enlarged and output to %s\n", OUT_FILE);
    enlarge_image(OUT_FILE, bitmap);

    // unload image
    if (bitmap) {
        FreeImage_Unload(bitmap);
    }

    return 0;
}
