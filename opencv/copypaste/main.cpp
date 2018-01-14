#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
#ifdef USE_JSON
#include <fstream>
#include <json.hpp>
#include <unistd.h>
#endif

#define JSON_FILE    "../setting.json"
#define INPUT_IMAGE  "lena.jpg"
#define OUTPUT_IMAGE "out.png"

using namespace cv;
using namespace std;

string input_img;
string output_img;

#ifdef USE_JSON
bool is_file_exist(const string& fn)
{
    if (access(fn.c_str(), F_OK) != -1) {
        return true;
    } else {
        return false;
    }
}

bool load_json(const string& json_file,
               string& input_fn,
               string& output_fn)
{
    if (!is_file_exist(JSON_FILE)) {
        cout << "json not found..." << endl;
        return false;
    }
    nlohmann::json json;
    try {
        ifstream infile(JSON_FILE);
        infile >> json;

        string datadir = json.at("datadir");
        input_fn = json.at("input");
        input_fn = datadir + '/' + input_fn;
        output_fn = json.at("output");
        cout << "input: " << input_fn << endl;
        cout << "output: " << output_fn << endl;
    } catch (nlohmann::json::parse_error& e) {
        cout << "parse json error: " << e.what();
        return false;
    }
    return true;
}
#endif

void init()
{
    namedWindow("src", WINDOW_AUTOSIZE);
    namedWindow("dst", WINDOW_AUTOSIZE);
    moveWindow("src", 0, 0);
    moveWindow("dst", 400, 0);
#ifdef USE_JSON
    if ( !load_json(JSON_FILE, input_img, output_img) ) {
        input_img = INPUT_IMAGE;
        output_img = OUTPUT_IMAGE;
    }
#else
    input_img = INPUT_IMAGE;
    output_img = OUTPUT_IMAGE;
#endif
}

Mat rotate(Mat src, double angle)
{
    Mat dst;
    Point2f pt(src.cols/2., src.rows/2.);
    Mat r = getRotationMatrix2D(pt, angle, 1.0);
    warpAffine(src, dst, r, Size(src.cols, src.rows));
    return dst;
}

int main()
{
    init();

    Mat src = imread(input_img);
    Mat dst = rotate(src, 45);

    imshow("src", src);
    imshow("dst", dst);

    imwrite(output_img, dst);

    waitKey(0);
    destroyAllWindows();

    return 0;
}
