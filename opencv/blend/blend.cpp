#include <stdio.h>
#include "opencv2/opencv.hpp"

using namespace cv;

/// Global Variables
const int alpha_slider_max = 100;
int alpha_slider;
double alpha;
double beta;

/// Matrices to store images
Mat src1;
Mat src2;
Mat dst;

/**
 * @function on_trackbar
 * @brief Callback for trackbar
 */
void on_trackbar( int, void* )
{
    alpha = (double) alpha_slider/alpha_slider_max;
    beta = ( 1.0 - alpha );

    addWeighted( src1, alpha, src2, beta, 0.0, dst);

    imshow( "Linear Blend", dst );
}

bool if_file_fxists(const char* fn)
{
    FILE* fptr = fopen(fn, "rb");
    if (fptr == NULL) {
        return false;
    } else {
        fclose(fptr);
        return true;
    }
}

void check_and_load(const char* fn, Mat& mat)
{
    if (if_file_fxists(fn)) {
        mat = imread(fn);
    } else {
        fprintf(stderr, "file not found: %s\n", fn);
        exit(-1);
    }
    if (!mat.data) {
        fprintf(stderr, "mat data error\n");
        exit(-2);
    }
}

int main( int argc, char** argv )
{
    const char image1[] = "LinuxLogo.jpg";
    const char image2[] = "WindowsLogo.jpg";

    check_and_load(image1, src1);
    check_and_load(image2, src2);

    /// Initialize values
    alpha_slider = 50;

    /// Create Windows
    namedWindow("Linear Blend", 1);

    /// Create Trackbars
    char TrackbarName[50];
    sprintf( TrackbarName, "Alpha x %d", alpha_slider_max );

    createTrackbar( TrackbarName, "Linear Blend", &alpha_slider, alpha_slider_max, on_trackbar );

    /// Show some stuff
    on_trackbar( alpha_slider, 0 );

    /// Wait until user press some key
    waitKey(0);
    return 0;
}
