/**
 * \file qibla.cpp
 */
#include <math.h>

double get_qibla_angle(double longitude, double latitude)
{
    double m = sin(longitude - 39.8230);
    double n = cos(latitude) * tan(21.42330) - sin(latitude) * cos(longitude - 39.8230);
    double q = atan(m/n);
    return q;
}
