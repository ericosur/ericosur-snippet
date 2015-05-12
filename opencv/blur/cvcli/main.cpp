// reference:
// http://blogs.wcode.org/2014/10/howto-install-build-and-use-opencv-macosx-10-10/

#include <unistd.h>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;

const string WINDOW_ORIGIN = "Unprocessed Image";
const string WINDOW_PROCESS = "Processed Image";
#if defined(__APPLE__)
const string DEFAULT_IAMGE = "/Users/ericosur/gcode/snippet/opencv/blur/deer.jpg";
#endif
#if defined(__linux__)
const string DEFAULT_IAMGE = "/home/rasmus/gcode/snippet/opencv/blur/deer.jpg";
#endif

const int GAUSSIAN_RADIUS = 29;

// load image into Mat, will check file exist or not
bool load_image(Mat& img, const string& fn)
{
    cout << "load image: " << fn << endl;
    if (access(fn.c_str(), F_OK) != -1) {
        // file exists
        img = imread(fn);
        return true;
    }

    // file not exist
    return false;
}

int main( int argc, char** argv )
{
    Mat src;
    Mat dst;

    // Load the source image
    bool ret = false;
    if (argc >= 2) {
        ret = load_image(src, argv[1]);
    } else {
        ret = load_image(src, DEFAULT_IAMGE);
    }

    if (!ret) {
        cout << "cannot load image, exit...\n";
        return -1;
    }

    namedWindow( WINDOW_ORIGIN, WINDOW_AUTOSIZE );
    imshow(WINDOW_ORIGIN, src);

    dst = src.clone();
    GaussianBlur( src, dst, Size(GAUSSIAN_RADIUS, GAUSSIAN_RADIUS), 0, 0 );

    namedWindow( WINDOW_PROCESS, WINDOW_AUTOSIZE );
    imshow(WINDOW_PROCESS, dst);

    waitKey();
    return 0;
}
