#include <iostream>

#include <opencv2/core/core.hpp>
#include <opencv2/opencv.hpp>

#ifdef USE_MYTOOL
#include <mytool/mytool.h>
#endif

using namespace std;
using namespace cv;
//this program is used for testing opencv encode and decode for jgeg pictures

/**
 ** refer to: https://stackoverflow.com/questions/259297/how-do-you-copy-the-contents-of-an-array-to-a-stdvector-in-c-without-looping
 **
 **/

typedef unsigned char byte;

int main()
{
    Mat tstMat = imread("../lena.jpg");
    //imshow("picture",tstMat);
    //waitKey(0);

    vector<byte> inImage;
    imencode(".jpg", tstMat, inImage);
    size_t datalen = inImage.size();
    cout << "datalen: " << datalen << "\n";

    byte* buffer = (byte*)malloc(inImage.size());
    std::copy(inImage.begin(), inImage.end(), buffer);
#ifdef USE_MYTOOL
    mytoolbox::dump((const char*)buffer, datalen);
#endif
    vector<unsigned char> buffVec;
    buffVec.insert(buffVec.end(), &buffer[0], &buffer[datalen]);
    Mat show = imdecode(buffVec, CV_LOAD_IMAGE_COLOR);

    imshow("copied", show);
    cv::waitKey(0);
    free(buffer);

    cout<<"hello world"<<endl;
    return 0;
}
