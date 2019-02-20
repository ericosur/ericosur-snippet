#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/freetype.hpp>

#define TTF_PATH  "/home/rasmus/Dropbox/app/font/monaco.ttf"

void test()
{
  using namespace cv;

  String text = "Funny text inside the box";
  int fontHeight = 60;
  int thickness = -1;
  int linestyle = 8;
  Mat img(600, 800, CV_8UC3, Scalar::all(0));
  int baseline=0;
  cv::Ptr<cv::freetype::FreeType2> ft2;
  ft2 = cv::freetype::createFreeType2();
  ft2->loadFontData( TTF_PATH, 0 );
  Size textSize = ft2->getTextSize(text,
                                   fontHeight,
                                   thickness,
                                   &baseline);
  if(thickness > 0){
      baseline += thickness;
  }
  // center the text
  Point textOrg((img.cols - textSize.width) / 2,
                (img.rows + textSize.height) / 2);
  // draw the box
  rectangle(img, textOrg + Point(0, baseline),
            textOrg + Point(textSize.width, -textSize.height),
            Scalar(0,255,0),1,8);
  // ... and the baseline first
  line(img, textOrg + Point(0, thickness),
       textOrg + Point(textSize.width, thickness),
       Scalar(0, 0, 255),1,8);
  // then put the text itself
  ft2->putText(img, text, textOrg, fontHeight,
               Scalar::all(255), thickness, linestyle, true );

  imshow("result", img);
  waitKey(0);
}

int main()
{
  test();
  cv::destroyAllWindows();
}
