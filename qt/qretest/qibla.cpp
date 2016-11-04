/**
 * \file qibla.cpp
 */
#include <math.h>

static const double DEG2RAD = 0.017453292519943295769236907684886;
static const double MECCA_LONGITUDE = 39.8230*DEG2RAD; // 39.8230E
static const double MECCA_LATITUDE = 21.42330*DEG2RAD; // 21.42330N
double get_qibla_angle(double longitude, double latitude)
{
    double m = sin(longitude*DEG2RAD - MECCA_LONGITUDE);
    double n = cos(latitude*DEG2RAD) * tan(MECCA_LATITUDE) - sin(latitude*DEG2RAD) * cos(longitude*DEG2RAD - MECCA_LONGITUDE);
    double q = atan(m/n) / DEG2RAD;
    return q;
}
