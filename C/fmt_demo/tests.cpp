/// \file: tests.cpp
///

#include "tests.h"

#include <iostream>
#include <limits>
#include <math.h>

// fmt:print()
#include <fmt/core.h>

// how to use & sample:
// https://fmt.dev/latest/index.html
// how to link and build:
// https://fmt.dev/latest/usage.html
// python format usage:
// https://github.com/gto76/python-cheatsheet#format
//
void test_fmt()
{
    // use fmt::print() like python fmt
    fmt::print(">>>>> enter {}:\n", __func__);

    const int levels = 12;
    double r = pow(2.0, 1.0/(double)levels);
    fmt::print("power: {}\n", r);
    double v = 1.0;
    for (int i = 0; i <= levels; i++) {
        fmt::print("[{:.>4d}] result: {:.3f}\n", i, v);
        v *= r;
    }
    std::cout << "---------------------\n";
    fmt::print("should show **inf**: {}", std::numeric_limits<double>::infinity());
    fmt::print("\n<<<<< build: {1} {2}, exit {0}\n", __func__, __DATE__, __TIME__);
}
