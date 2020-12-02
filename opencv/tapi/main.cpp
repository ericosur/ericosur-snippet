#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;

template <class T>
void show_and_wait(const char* title, const T& img)
{
    imshow(title, img);
    waitKey();
}

int test1(const char* imgfn)
{
    using namespace std;

    Mat gray;
    Mat img = imread(imgfn, 1);
    if (img.empty()) {
        cout << "imread failed: " << imgfn << endl;
        return -1;
    }

    cvtColor(img, gray, COLOR_BGR2GRAY);
    GaussianBlur(gray, gray,Size(7, 7), 1.5);
    Canny(gray, gray, 0, 50);

    show_and_wait("test1", gray);
    return 0;
}


int test2(const char* imgfn)
{
    UMat img, gray;
    imread(imgfn, 1).copyTo(img);

    cvtColor(img, gray, COLOR_BGR2GRAY);
    GaussianBlur(gray, gray,Size(7, 7), 1.5);
    Canny(gray, gray, 0, 50);

    show_and_wait("test2", gray);
    return 0;
}

/*
int test3(const char* imgfn)
{
    Mat mat = imread(imgfn, IMREAD_COLOR);
    UMat umat = mat.getUMat(ACCESS_READ);
}
*/

int main(int argc, char** argv)
{
    using namespace std;

    const char imgfn[] = "image.jpg";

    if (argc == 1) {
        cout << "test1 " << imgfn << endl;
        assert(test1(imgfn)==0);
    } else {
        cout << "test2 " << imgfn << endl;
        assert(test2(imgfn)==0);
    }

    return 0;
}
