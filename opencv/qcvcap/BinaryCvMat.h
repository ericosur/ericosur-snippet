#ifndef __QCVCAP_BINARY_CV_MAT_H__
#define __QCVCAP_BINARY_CV_MAT_H__

#include <opencv2/core/core.hpp>
#include <fstream>

bool SaveMatBinary(const std::string& filename, const cv::Mat& output);
bool LoadMatBinary(const std::string& filename, cv::Mat& output);

#endif  // __QCVCAP_BINARY_CV_MAT_H__
