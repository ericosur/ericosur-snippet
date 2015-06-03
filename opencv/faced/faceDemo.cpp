//#include <opencv2/opencv.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <cctype>
#include <iostream>
#include <iterator>
#include <stdio.h>

using namespace std;
using namespace cv;

void detectAndDraw( Mat& img, CascadeClassifier& cascade,
                    CascadeClassifier& nestedCascade,
                    double scale, bool tryflip );

//const string cascadeName = "/Users/ericosur/haarcascade_frontalface_alt.xml";
const string cascadeName = "./haarcascade_frontalface_alt.xml";
//const string nestedCascadeName = "/Users/ericosur/haarcascade_eye_tree_eyeglasses.xml";
const string nestedCascadeName = "./haarcascade_eye_tree_eyeglasses.xml";
//const string inputName = "/Users/ericosur/lena.jpg";
const string inputName = "./lena.jpg";

#if 1
//int face_detect_camera()
int face_detect()
{
    //default capture width and height
    const int FRAME_WIDTH = 1280;
    const int FRAME_HEIGHT = 720;
    const int WAIT_DELAY = 100;

    cout << "face_detect_camera()\n";

    Mat frame, image;
    CascadeClassifier cascade, nestedCascade;
    bool tryflip = false;
    double scale = 1.3;

    if ( nestedCascade.load( nestedCascadeName ) ) {
        cerr << "load nestedCascadeName ok" << endl;
    } else {
        cerr << "WARNING: Could not load classifier cascade for nested objects" << endl;
    }

    if ( cascade.load( cascadeName ) ) {
        cerr << "load cascadeName ok" << endl;
    } else {
        cerr << "ERROR: Could not load classifier cascade" << endl;
        return -1;
    }

    VideoCapture capture;
    capture.open(0);
    if (!capture.isOpened()) {
        cerr << "Error: capture is not opened" << endl;
        return -1;
    }

    cvNamedWindow( "result", 1 );
    // set height and width of capture frame
    capture.set(CV_CAP_PROP_FRAME_WIDTH, FRAME_WIDTH);
    capture.set(CV_CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT);

    while (true) {
        capture.read(frame);
        image = frame.clone();
        detectAndDraw( image, cascade, nestedCascade, scale, tryflip );
        if ( waitKey(WAIT_DELAY) > 0 ) {
            cvDestroyAllWindows();
            break;
        }
    };

    return 0;
}
#else
// face detect from image
int face_detect()
{
    cout << "face_detect()\n";

    Mat frame, frameCopy, image;
    CascadeClassifier cascade, nestedCascade;
    bool tryflip = false;
    double scale = 1.3;

    if ( nestedCascade.load( nestedCascadeName ) ) {
        cerr << "load nestedCascadeName ok" << endl;
    } else {
        cerr << "WARNING: Could not load classifier cascade for nested objects" << endl;
    }

    if ( cascade.load( cascadeName ) ) {
        cerr << "load cascadeName ok" << endl;
    } else {
        cerr << "ERROR: Could not load classifier cascade" << endl;
        return -1;
    }

    image = imread( inputName, 1 );
    if ( image.empty() ) {
        cerr << "image is empty" << endl;
    } else {
        cerr << "image is loaded" << endl;
    }

    cvNamedWindow( "result", 1 );

    do {
        cout << "In image read" << endl;
        if ( !image.empty() ) {
            detectAndDraw( image, cascade, nestedCascade, scale, tryflip );
            //waitKey(0);
        }
    } while (0);

    if (waitKey(0) > 0) {
        //cvDestroyWindow("result");
        cvDestroyAllWindows();
    }

    return 0;
}
#endif

void detectAndDraw( Mat& img, CascadeClassifier& cascade,
                    CascadeClassifier& nestedCascade,
                    double scale, bool tryflip )
{
    //cout << "detectAndDraw..." << endl;
    int i = 0;
    double t = 0;
    vector<Rect> faces, faces2;
    const static Scalar colors[] =  { CV_RGB(0,0,255),
        CV_RGB(0,128,255),
        CV_RGB(0,255,255),
        CV_RGB(0,255,0),
        CV_RGB(255,128,0),
        CV_RGB(255,255,0),
        CV_RGB(255,0,0),
        CV_RGB(255,0,255)} ;
    Mat gray, smallImg( cvRound (img.rows/scale), cvRound(img.cols/scale), CV_8UC1 );

    cvtColor( img, gray, COLOR_BGR2GRAY );
    resize( gray, smallImg, smallImg.size(), 0, 0, INTER_LINEAR );
    equalizeHist( smallImg, smallImg );

    t = (double)cvGetTickCount();
    cascade.detectMultiScale( smallImg, faces,
        1.1, 2, 0
        //|CASCADE_FIND_BIGGEST_OBJECT
        //|CASCADE_DO_ROUGH_SEARCH
        |CASCADE_SCALE_IMAGE
        ,
        Size(30, 30) );

    if ( tryflip ) {
        cout << "yes, try flip\n";
        flip(smallImg, smallImg, 1);
        cascade.detectMultiScale( smallImg, faces2,
                                 1.1, 2, 0
                                 //|CASCADE_FIND_BIGGEST_OBJECT
                                 //|CASCADE_DO_ROUGH_SEARCH
                                 |CASCADE_SCALE_IMAGE
                                 ,
                                 Size(30, 30) );
        for ( vector<Rect>::const_iterator r = faces2.begin(); r != faces2.end(); r++ )
        {
            faces.push_back(Rect(smallImg.cols - r->x - r->width, r->y, r->width, r->height));
        }
    }
    t = (double)cvGetTickCount() - t;
    char mytext[60];
    sprintf( mytext, "%g ms", t/((double)cvGetTickFrequency()*1000.) );
    putText(img, mytext, cvPoint(40, 100), FONT_HERSHEY_PLAIN,
            4.0, CV_RGB(255,0,0), 2);
    for( vector<Rect>::const_iterator r = faces.begin(); r != faces.end(); r++, i++ )
    {
        Mat smallImgROI;
        vector<Rect> nestedObjects;
        Point center;
        Scalar color = colors[i%8];
        int radius;

        double aspect_ratio = (double)r->width/r->height;
        if( 0.75 < aspect_ratio && aspect_ratio < 1.3 )
        {
            center.x = cvRound((r->x + r->width*0.5)*scale);
            center.y = cvRound((r->y + r->height*0.5)*scale);
            radius = cvRound((r->width + r->height)*0.25*scale);
            //circle( img, center, radius, color, 3, 8, 0 );
            rectangle( img, cvPoint(cvRound(r->x*scale), cvRound(r->y*scale)),
                       cvPoint(cvRound((r->x + r->width-1)*scale), cvRound((r->y + r->height-1)*scale)),
                       color, 3, 8, 0);
        }
        else {
            rectangle( img, cvPoint(cvRound(r->x*scale), cvRound(r->y*scale)),
                       cvPoint(cvRound((r->x + r->width-1)*scale), cvRound((r->y + r->height-1)*scale)),
                       color, 3, 8, 0);
        }
        if ( nestedCascade.empty() )
            continue;
        smallImgROI = smallImg(*r);
        nestedCascade.detectMultiScale( smallImgROI, nestedObjects,
            1.1, 2, 0
            //|CASCADE_FIND_BIGGEST_OBJECT
            //|CASCADE_DO_ROUGH_SEARCH
            //|CASCADE_DO_CANNY_PRUNING
            |CASCADE_SCALE_IMAGE
            ,
            Size(30, 30) );
        for ( vector<Rect>::const_iterator nr = nestedObjects.begin(); nr != nestedObjects.end(); nr++ ) {
            center.x = cvRound((r->x + nr->x + nr->width*0.5)*scale);
            center.y = cvRound((r->y + nr->y + nr->height*0.5)*scale);
            radius = cvRound((nr->width + nr->height)*0.25*scale);
            circle( img, center, radius, color, 3, 8, 0 );
        }
    }
    cv::imshow( "result", img );
    //cout << "end of function\n";
}
