//objectTrackingTutorial.cpp

//Written by  Kyle Hounslow 2013

//Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software")
//, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
//and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

//The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
//IN THE SOFTWARE.

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <iostream>
#include <sstream>
#include <string>

#ifdef USE_JSON
#include <fstream>
#include <json.hpp>
#include <unistd.h>
#define JSON_FILE    "../setting.json"
#endif

using namespace cv;
using namespace std;

int video_id = 0;

#ifdef USE_JSON
bool is_file_exist(const string& fn)
{
    if (access(fn.c_str(), F_OK) != -1) {
        return true;
    } else {
        return false;
    }
}

bool load_json(const string& json_file)
{
    if (!is_file_exist(JSON_FILE)) {
        cout << "json not found..." << endl;
        return false;
    }
    nlohmann::json json;
    try {
        ifstream infile(JSON_FILE);
        infile >> json;

        video_id = json.at["video_id"];
        cout << "video_id: " << video_id << endl;
    } catch (nlohmann::json::parse_error& e) {
        cout << "parse json error: " << e.what();
        return false;
    }
    return true;
}
#endif

//initial min and max HSV filter values.
//these will be changed using trackbars
//const int H_MIN = 0;
const int H_MAX = 180;
//const int S_MIN = 0;
const int S_MAX = 255;
//const int V_MIN = 0;
const int V_MAX = 255;

int h_min = 0;
int h_max = 50;
int s_min = 0;
int s_max = 30;
int v_min = 0;
int v_max = 255;

//default capture width and height
const int FRAME_WIDTH = 320;
const int FRAME_HEIGHT = 240;
//max number of objects to be detected in frame
const int MAX_NUM_OBJECTS = 10;
//minimum and maximum object area
const int MIN_OBJECT_AREA = 20 * 20;
const int MAX_OBJECT_AREA = FRAME_HEIGHT * FRAME_WIDTH / 2;
//names that will appear at the top of each window
const string WINDOW_ORIGIN = "Original Image";
const string WINDOW_HSV = "HSV Image";
const string WINDOW_THRESHOLD = "Thresholded Image";
const string WINDOW_MORPH = "After Morphological Operations";
const string WINDOW_TRACKBAR = "Trackbars";



void on_trackbar(int, void*)
{
    // This function gets called whenever a
	// trackbar position is changed
}

string intToString(int number)
{
	std::stringstream ss;
	ss << number;
	return ss.str();
}

void createTrackbars()
{
	//create window for trackbars
    namedWindow(WINDOW_TRACKBAR, 0);

	//create trackbars and insert them into window
	//3 parameters are: the address of the variable that is changing when the trackbar is moved(eg.H_LOW),
	//the max value the trackbar can move (eg. H_HIGH),
	//and the function that is called whenever the trackbar is moved(eg. on_trackbar)
	//                                  ---->    ---->     ---->
    createTrackbar("H_MIN", WINDOW_TRACKBAR, &h_min, H_MAX, on_trackbar);
    createTrackbar("H_MAX", WINDOW_TRACKBAR, &h_max, H_MAX, on_trackbar);
    createTrackbar("S_MIN", WINDOW_TRACKBAR, &s_min, S_MAX, on_trackbar);
    createTrackbar("S_MAX", WINDOW_TRACKBAR, &s_max, S_MAX, on_trackbar);
    createTrackbar("V_MIN", WINDOW_TRACKBAR, &v_min, V_MAX, on_trackbar);
    createTrackbar("V_MAX", WINDOW_TRACKBAR, &v_max, V_MAX, on_trackbar);
}

void drawObject(int x, int y, Mat &frame)
{
	//use some of the openCV drawing functions to draw crosshairs
	//on your tracked image!

	//UPDATE:JUNE 18TH, 2013
	//added 'if' and 'else' statements to prevent
	//memory errors from writing off the screen (ie. (-25,-25) is not within the window!)

	circle(frame, Point(x, y), 20, Scalar(0, 255, 0), 2);
	if (y - 25>0)
		line(frame, Point(x, y), Point(x, y - 25), Scalar(0, 255, 0), 2);
	else line(frame, Point(x, y), Point(x, 0), Scalar(0, 255, 0), 2);
	if (y + 25<FRAME_HEIGHT)
		line(frame, Point(x, y), Point(x, y + 25), Scalar(0, 255, 0), 2);
	else line(frame, Point(x, y), Point(x, FRAME_HEIGHT), Scalar(0, 255, 0), 2);
	if (x - 25>0)
		line(frame, Point(x, y), Point(x - 25, y), Scalar(0, 255, 0), 2);
	else line(frame, Point(x, y), Point(0, y), Scalar(0, 255, 0), 2);
	if (x + 25<FRAME_WIDTH)
		line(frame, Point(x, y), Point(x + 25, y), Scalar(0, 255, 0), 2);
	else line(frame, Point(x, y), Point(FRAME_WIDTH, y), Scalar(0, 255, 0), 2);

	putText(frame, intToString(x) + "," + intToString(y), Point(x, y + 30), 1, 1, Scalar(0, 255, 0), 2);
}

void morphOps(Mat &thresh)
{
	//create structuring element that will be used to "dilate" and "erode" image.
	//the element chosen here is a 3px by 3px rectangle

	Mat erodeElement = getStructuringElement(MORPH_RECT, Size(3, 3));
	//dilate with larger element so make sure object is nicely visible
	Mat dilateElement = getStructuringElement(MORPH_RECT, Size(8, 8));

	erode(thresh, thresh, erodeElement);
	erode(thresh, thresh, erodeElement);

	dilate(thresh, thresh, dilateElement);
	dilate(thresh, thresh, dilateElement);
}

void trackFilteredObject(int &x, int &y, Mat threshold, Mat &cameraFeed)
{
	Mat temp;
	threshold.copyTo(temp);
	//these two vectors needed for output of findContours
	vector< vector<Point> > contours;
	vector<Vec4i> hierarchy;
	//find contours of filtered image using openCV findContours function
	findContours(temp, contours, hierarchy, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE);
	//use moments method to find our filtered object
	double refArea = 0;
	bool objectFound = false;
	if (hierarchy.size() > 0) {
		int numObjects = hierarchy.size();
		//if number of objects greater than MAX_NUM_OBJECTS we have a noisy filter
		if (numObjects<MAX_NUM_OBJECTS){
			for (int index = 0; index >= 0; index = hierarchy[index][0]) {

				Moments moment = moments((cv::Mat)contours[index]);
				double area = moment.m00;

				//if the area is less than 20 px by 20px then it is probably just noise
				//if the area is the same as the 3/2 of the image size, probably just a bad filter
				//we only want the object with the largest area so we safe a reference area each
				//iteration and compare it to the area in the next iteration.
				if (area>MIN_OBJECT_AREA && area<MAX_OBJECT_AREA && area>refArea){
					x = moment.m10 / area;
					y = moment.m01 / area;
					objectFound = true;
					refArea = area;
				}
				else objectFound = false;


			}
			//let user know you found an object
			if (objectFound == true){
				putText(cameraFeed, "Tracking Object", Point(0, 50), 2, 1, Scalar(0, 255, 0), 2);
				//draw object location on screen
				drawObject(x, y, cameraFeed);
			}

		}
		else putText(cameraFeed, "TOO MUCH NOISE! ADJUST FILTER", Point(0, 50), 1, 2, Scalar(0, 0, 255), 2);
	}
}

int demoCapture()
{
	//some boolean variables for different functionality within this program
    //bool trackObjects = false;
    //bool useMorphOps = false;
    //x and y values for the location of the object
    //int x = 0, y = 0;

	//Matrix to store each frame of the webcam feed
	Mat cameraFeed;
	//matrix storage for HSV image
	Mat HSV;
	//matrix storage for binary threshold image
	Mat threshold;
	//create slider bars for HSV filtering
	createTrackbars();
	//video capture object to acquire webcam feed
	VideoCapture capture;
	//open capture object at location zero (default location for webcam)
	capture.open(video_id);

    if (!capture.isOpened()) {
    	cerr << "VideoCapture not opened...\n";
        return -1;
    }

	//set height and width of capture frame
	capture.set(CV_CAP_PROP_FRAME_WIDTH, FRAME_WIDTH);
	capture.set(CV_CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT);

    // create namedWindows
    namedWindow(WINDOW_ORIGIN, WINDOW_AUTOSIZE);
    namedWindow(WINDOW_HSV, WINDOW_AUTOSIZE);
    namedWindow(WINDOW_THRESHOLD, WINDOW_AUTOSIZE);

	//start an infinite loop where webcam feed is copied to cameraFeed matrix
	//all of our operations will be performed within this loop
	while (true) {
		//store image to matrix
		capture.read(cameraFeed);
		//convert frame from BGR to HSV colorspace
		cvtColor(cameraFeed, HSV, COLOR_BGR2HSV);
		//filter HSV image between values and store filtered image to
		//threshold matrix
		inRange(HSV, Scalar(h_min, s_min, v_min), Scalar(h_max, s_max, v_max), threshold);
#if 0
		//perform morphological operations on thresholded image to eliminate noise
		//and emphasize the filtered object(s)
		if (useMorphOps)
			morphOps(threshold);
		//pass in thresholded frame to our object tracking function
		//this function will return the x and y coordinates of the
		//filtered object
		if (trackObjects)
			trackFilteredObject(x, y, threshold, cameraFeed);
#endif
		// draw something
		//drawSomething(cameraFeed);
		//drawObject(50, 50, cameraFeed);

		//show frames
        imshow(WINDOW_THRESHOLD, threshold);
        imshow(WINDOW_ORIGIN, cameraFeed);
        imshow(WINDOW_HSV, HSV);

		//delay 30ms so that screen can refresh.
		//image will not appear without this waitKey() command
        int c = waitKey(100);
        if (c == 'c') {
            destroyAllWindows();
            break;
        }
	}

    capture.release();
	return 0;
}

int demoTest()
{
    const string WIN_FEED = "camera feeds";
    const string WIN_EDGE = "edges";

#ifdef USE_JSON
    if ( !load_json(JSON_FILE) )
#else
    video_id = 0;
#endif

    VideoCapture cap;
    cap.open(video_id);
    if (!cap.isOpened()) {
        cout << "open capture device failed\n";
        return -1;
    }

    Mat cameraFeed;
    Mat edges;

    namedWindow(WIN_FEED, WINDOW_AUTOSIZE);
    namedWindow(WIN_EDGE, WINDOW_AUTOSIZE);

    //set height and width of capture frame
    cap.set(CV_CAP_PROP_FRAME_WIDTH, FRAME_WIDTH);
    cap.set(CV_CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT);

    while (true) {
        //store image to matrix
        cap.read(cameraFeed);
        imshow(WIN_FEED, cameraFeed);

        cvtColor(cameraFeed, edges, CV_BGR2GRAY);
        GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
        Canny(edges, edges, 0, 30, 3);
        imshow(WIN_EDGE, edges);

        if ( waitKey(100) > 0 ) {
            destroyAllWindows();
            break;
        }
    }
    return 0;
}
