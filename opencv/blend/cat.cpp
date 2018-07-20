#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core.hpp>

using namespace std;
using namespace cv;

int main()
{
    cv::Mat a = (cv::Mat_<int>(2,2)<<1,2,3,4);
    cv::Mat b = (cv::Mat_<int>(2,2)<<5,6,7,8);
    cv::Mat c = (cv::Mat_<int>(2,2)<<9,10,11,12);
    cv::Mat d = (cv::Mat_<int>(2,2)<<13,14,15,16);
    Mat combine,combine1,combine2;
    hconcat(a,b,combine1);
    hconcat(c,d,combine2);
    vconcat(combine1,combine2,combine);
    //namedWindow("Combine",CV_WINDOW_AUTOSIZE);
    //imshow("Combine",combine);
    cout<<"Combine=:"<<combine<<endl;
    return 0;
}

/*

#include <iostream>
#include <core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
using namespace std;
using namespace cv;
int main()
{
    //cv::Mat a = (cv::Mat_<int>(2,2)<<1,2,3,4);
    //cv::Mat b = (cv::Mat_<int>(2,2)<<5,6,7,8);
    //cv::Mat c = (cv::Mat_<int>(2,2)<<9,10,11,12);
    //cv::Mat d = (cv::Mat_<int>(2,2)<<13,14,15,16);
    Mat combine,combine1,combine2;
    Mat a=imread("1.jpg");
    Mat b=imread("2.jpg");
    Mat c=imread("3.jpg");
    Mat d=imread("4.jpg");
    hconcat(a,b,combine1);
    hconcat(c,d,combine2);
    vconcat(combine1,combine2,combine);
    namedWindow("Combine",CV_WINDOW_AUTOSIZE);
    imshow("Combine",combine);
    waitKey(0);
    //cout<<"Combine=:"<<combine<<endl;
    system("pause");
    return 0;
}

*/
