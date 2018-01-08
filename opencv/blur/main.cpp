// reference:
// http://blogs.wcode.org/2014/10/howto-install-build-and-use-opencv-macosx-10-10/

#include <unistd.h>
#include <iostream>
#include <opencv2/opencv.hpp>

#ifdef USE_JSON
#include <fstream>
#include <json.hpp>
#endif

using namespace std;
using namespace cv;

const string WINDOW_ORIGIN = "Unprocessed Image";
const string WINDOW_PROCESS = "Processed Image";
const string DEFAULT_IAMGE = "deer.jpg";

int GAUSSIAN_RADIUS = 29;

bool is_file_exist(const string& fn);

#ifdef USE_JSON

const string JSON_FILE = "../setting.json";

bool load_json(string& img_file)
{
    if (!is_file_exist(JSON_FILE)) {
        cout << "json not found..." << endl;
        return false;
    }
    nlohmann::json json;
    try {
        ifstream infile(JSON_FILE);
        infile >> json;
        cout << "input image: " << json.at("image") << endl;
        img_file = json.at("image");
    } catch (nlohmann::json::parse_error& e) {
        cout << "parse json error: " << e.what();
        return false;
    }
    try {
        GAUSSIAN_RADIUS = json.at("radius");
    } catch (nlohmann::json::out_of_range& e) {
        GAUSSIAN_RADIUS = 29;
    }
    cout << "gaussian radius: " << GAUSSIAN_RADIUS << endl;
    return true;
}
#endif

bool is_file_exist(const string& fn)
{
    if (access(fn.c_str(), F_OK) != -1) {
        return true;
    } else {
        return false;
    }
}

// load image into Mat, will check file exist or not
bool load_image(Mat& img, const string& fn)
{
    cout << "load image: " << fn << endl;
    if (is_file_exist(fn)) {
        // file exists
        //cout << "file exists..." << endl;
        img = imread(fn);
        return true;
    }

    // file not exist
    return false;
}


int main( int argc, char** argv )
{
    string img_file = DEFAULT_IAMGE;

#ifdef USE_JSON
    load_json(img_file);
#endif
    if (argc > 1) {
        img_file = argv[1];
    }

    Mat src;
    Mat dst;

    if (!load_image(src, img_file)) {
        cout << "cannot load image, exit...\n";
        return -1;
    }

    namedWindow( WINDOW_ORIGIN, WINDOW_AUTOSIZE );
    imshow(WINDOW_ORIGIN, src);

    dst = src.clone();
    GaussianBlur( src, dst, Size(GAUSSIAN_RADIUS, GAUSSIAN_RADIUS), 0, 0 );

    namedWindow( WINDOW_PROCESS, WINDOW_AUTOSIZE );
    imshow(WINDOW_PROCESS, dst);

    cout << "press any key to exit..." << endl;
    waitKey();
    return 0;
}
