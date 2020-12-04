
/*
(d+=m<3?y--:y-2,23*m/9+d+4+y/4-y/100+y/400)%7
 */

#define MIN_YEAR_TO_WORK    1600

bool check_validity(int y, int m, int d)
{
    if (y < 1752) {
        return false;
    }
    if (y == 1752) {
        if (m < 9) {
            return false;
        }
        if (m == 9 && d < 14) {
            return false;
        }
    }
    return true;
}

// 0: sun, 1: mon, 2: tue, 3: wed, 4: thu, 5: fri, 6: sat
int dow(int y, int m, int d)
{
    if (!check_validity(y, m, d)) {
        return -1;
    }
    return ((d+=m<3?y--:y-2,23*m/9+d+4+y/4-y/100+y/400)%7);
}

// 0: sun, 1: mon, 2: tue, 3: wed, 4: thu, 5: fri, 6: sat
int dow2(int y, int m, int d)
{
    if (!check_validity(y, m, d)) {
        return -1;
    }
    d += m<3 ? y-- : y-2;
    return ((23*m/9+d+4+y/4-y/100+y/400)%7);
}
