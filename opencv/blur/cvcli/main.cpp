// reference:
// http://blogs.wcode.org/2014/10/howto-install-build-and-use-opencv-macosx-10-10/

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;

const char window_name1[] = "Unprocessed Image";
const char window_name2[] = "Processed Image";
const char default_img[] = "deer.jpg";

int main( int argc, char** argv )
{
    Mat src;
    Mat dst;

    // Load the source image
    if (argc >= 2) {
        src = imread(argv[1], 1);
    } else {
        src = imread(default_img, 1);
    }

    namedWindow( window_name1, WINDOW_AUTOSIZE );
    imshow("Unprocessed Image", src);

    dst = src.clone();
    GaussianBlur( src, dst, Size( 15, 15 ), 0, 0 );

    namedWindow( window_name2, WINDOW_AUTOSIZE );
    imshow("Processed Image", dst);

    waitKey();
    return 0;
}
