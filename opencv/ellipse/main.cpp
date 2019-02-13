#include "hsv2rgb.h"
#include <stdio.h>
#include <math.h>
#include <unistd.h>
#include <opencv2/opencv.hpp>

#define MAX_WIDTH   800
#define MAX_HEIGHT  800
#define MAX_COUNT   100
#define MAX_DEGREE  360
#define DELAY_TIME  500

inline double rad2deg(double rad)
{
    return rad * 180.0 / M_PI;
}

inline double deg2rad(double deg)
{
    return deg * M_PI / 180.0;
}

void drawln(cv::Mat& img, cv::Point p1, cv::Point p2, cv::Scalar c = cv::Scalar(255,255,255))
{
    cv::line(img, p1, p2, c, 1);
}
void drawpt(cv::Mat& img, int x, int y, cv::Scalar c = cv::Scalar(255,255,255))
{
    cv::circle(img, cv::Point(x, y), 4, c, 2);
}
void swap(double& m, double& n)
{
    double tmp = m;
    m = n;
    n = tmp;
}
double epsilon(double a, double b)
{
    //printf("%s: a:%.2f b:%.2f\n", __func__, a, b);
    if (a < b) {
        swap(a, b);
    }
    double ep = sqrt(1.0 - (b*b)/(a*a));
    //printf("ep: %.2f\n", ep);
    return ep;
}
/**
 * see picture here:
 * [Imgur](https://i.imgur.com/lM7SRRu.png)
 *
 *  reference: https://zh.wikipedia.org/zh-tw/%E6%A4%AD%E5%9C%86
 */
void draw_ellipse()
{
    using namespace cv;
    const int sec_len = 40;
    const int space_len = 120;

    Mat img = Mat::zeros(MAX_WIDTH, MAX_HEIGHT, CV_8UC3);
    int m = MAX_WIDTH / 2;
    int n = MAX_HEIGHT / 2;
    int a1 = MAX_WIDTH / 2 - space_len;
    int b1 = MAX_HEIGHT / 3 - space_len;
    int a2 = a1 + sec_len;
    int b2 = b1 + sec_len;

    drawpt(img, m, n, Scalar(127,255,127));
    double ep1 = epsilon(a1, b1);
    double c1 = a1 * ep1;
    //printf("c1: %.2f\n", c1);
    drawpt(img, m + c1, n);
    drawpt(img, m - c1, n);

    int i = 0;
    hsv cc;
    rgb dd;
    cc.h = 0.0;
    cc.s = 1.0;
    cc.v = 255.0;

    //for (int i = 0; i < MAX_DEGREE; i+=3) {
    while (true) {
        float t = deg2rad(float(i));
        int x1 = m + a1 * cos(t);
        int y1 = n + b1 * sin(t);
        int x2 = m + a2 * cos(t);
        int y2 = n + b2 * sin(t);
        //printf("point at (%d, %d) for %d degree\n", x, y, i);
        //drawpt(img, x, y);
        cc.h = i;
        dd = hsv2rgb(cc);
        usleep(DELAY_TIME);
        drawln(img, Point(x1,y1), Point(x2,y2), Scalar(dd.r, dd.g, dd.b));
        imshow("result", img);
        i = (i + 3) % MAX_DEGREE;
        cc.v = (int(cc.v) + 1) % 255;
        int key = waitKey(1);
        if (key == 0x1B) {
            break;
        }
    }

    destroyAllWindows();
}

int main()
{
    draw_ellipse();
    return 0;
}
