// http://rosettacode.org/wiki/Haversine_formula#C

#include <iostream>
#include <fstream>
#include <sstream>
#include <limits>
#include <string>
#include <math.h>
#include <vector>
#include <cstdlib>
#include <unistd.h>

using namespace std;

#define R 6371
#define TO_RAD (3.1415926536 / 180)
#define TARGETPATH  "/etc/"
#define HOSTPATH    "./"
#define CITYLIST    "citieslist.txt"

/// @brief The usual PI/180 constant
static const double DEG_TO_RAD = 0.017453292519943295769236907684886;
/// @brief Earth's quatratic mean radius for WGS-84
static const double EARTH_RADIUS_IN_METERS = 6372.797560856;

const double preset_loc[][2] = {
    {25.033827, 121.565768},  // Taipei 101
    {-15.763250, -47.870459},   // Universidade de Brasília
    {37.421282, -122.086989},   // googleplex, mountain view CA
    {40.689201, -74.044382},    // staue of liberty
    {51.500760, -0.124296}, // Ben clock at London
    {35.658519, 139.745529},    // tokyo tower
    {29.975278, 31.138007}, // great sphinx
    {1.286859, 103.854854}, // merlion
    {-43.529076, 172.623976},   // north hagley park christchurch
    {21.361145, -157.948567},        // pearl harbor
    {-33.908068, 18.418042}, // two oceans aquarium
    {30.328448, 35.444428}, // petra jordan
    {-2.228088, 38.559125},// kitui
    {21.422399, 39.827339},// kaaba
};

// control flags
bool debug = false;
bool autotz = false;


double dist(double th1, double ph1, double th2, double ph2)
{
    double dx, dy, dz;
    ph1 -= ph2;
    ph1 *= DEG_TO_RAD, th1 *= DEG_TO_RAD, th2 *= DEG_TO_RAD;

    dz = sin(th1) - sin(th2);
    dx = cos(ph1) * cos(th1) - cos(th2);
    dy = sin(ph1) * cos(th1);
    return asin(sqrt(dx * dx + dy * dy + dz * dz) / 2) * 2 * EARTH_RADIUS_IN_METERS;
}

void usage()
{
    printf(
        "Usage: ./autotz  <-parameter>  latitude  longitude\n"
        "-h: this help screen\n"
        "-e: execute auto time zone , set timezone to device\n"
        "-d: print more debug message\n"
        "-t <nn>: test run on preset location #nn\n"
        "[no parameter]: just show the timezone on the screen\n"
        "\nExample:\n"
        "./autotz 23.5  122.5\n"
        "./autotz -e  23.5 122.5\n"
    );
}

int search_city_table(double inputlat, double inputlong)
{
    ifstream file(TARGETPATH CITYLIST);
    string linebuffer;
    vector<string> tokens;
    double latitude,longitude;
    string tmptz,location,finaltz;
    string pop;
    string curtz[2];
    double tmpdis=numeric_limits<double>::max();
    double d,dis[2],population[2];
    string token;
    string command;

    dis[0] = dis[1] = tmpdis;
    population[0] = population[1] = 0;


    if (file.fail()) {
        // try another path
        file.open(HOSTPATH CITYLIST);
        if (file.fail()) {
            // fail twice
            printf("autotz: error: cannot open data file\n");
            return false;
        }
    }

    while (file && getline(file, linebuffer)) {
        if (linebuffer.length() == 0)
            continue;
        istringstream iss(linebuffer);

        while(getline(iss, token, '\t'))   // but we can specify a different one
            tokens.push_back(token);

        latitude = atof(tokens[1].c_str());
        longitude = atof(tokens[2].c_str());

        d = dist(inputlat,inputlong,latitude,longitude);

        if (d <= tmpdis || d <= dis[1]) {
            tmpdis = d;
            tmptz = tokens[3];
            location = tokens[0];
            pop = tokens[4];
            //save the last two nearest dis
            if (tmpdis <  dis[1]) {
                if (tmpdis <  dis[0]) {
                    dis[1] = dis[0];
                    curtz[1] = curtz[0];
                    population[1] = population[0];
                    dis[0] = tmpdis;
                    curtz[0] = tmptz;
                    population[0] = atof(pop.c_str());
                } else { // dis[0] < d < dis[1]
                    dis[1] = tmpdis;
                    curtz[1] = tmptz;
                    population[1] = atof(pop.c_str());
                }
            }
            //if(debug)
                //printf("%.3f  tz:%s  loc:%s  pop:%s\n", d, tmptz.c_str() ,location.c_str(),pop.c_str());
        }
        tokens.clear();
    }
    finaltz = curtz[0];

    if (debug) {
        for (int i=1; i>=0; i--) {  // print nearest two location
            printf("%.3f  loc: %s tz:%s \n", dis[i], location.c_str(), curtz[i].c_str());
        }
    }

    command = "ln -sf /usr/share/timezone/zoneinfo/"+finaltz+" /etc/localtime";
    //printf("command:%s \n" ,command.c_str());
    if (autotz) {
        printf("copy time zone to /etc/localtime\n");
        if ( system(command.c_str()) ) {
            ;
        }
    }
    printf("autotz: predict time zone: %s\n",finaltz.c_str());

    return 0;
}

int main(int argc, char* argv[])
{

    bool testrun = false;
    int test_type = 0;
    int c;

    double inputlat = 0.0;
    double inputlong = 0.0;

    printf("autotz: %s %s\n", __DATE__, __TIME__);

    if (argc == 1) {
        usage();
        return 0;
    }

    while(1) {
        c = getopt(argc,argv,"hH?:det:");
        if (c == -1)
            break;
        //printf("c = %d %c\n",c,c);
        switch(c) {
        case 'h':
        case 'H':
        case '?':
            usage();
            return 0;
        case 'd' :
            debug = true;
            break;
        case 'e':
            autotz = true;
            break;
        case 't':
            if (optarg) {
                //printf("%s\n", optarg);
                test_type = strtol(optarg, NULL, 10);
                fprintf(stderr, "preset location: %d\n", test_type);
            }
            testrun = true;
            debug = true;
            break;
        default:
            break;
        }
    }

    if (argc > optind) {
        const int tmp_size = 2;
        double tmp[] = {0.0, 0.0};
        int ti = 0;
        for (int i = optind; i < argc; i++) {
            tmp[ti++] = atof(argv[i]);
            if (ti>=tmp_size)
                break;
        }
        inputlat = tmp[0];
        inputlong = tmp[1];
    } else if (testrun) {
        printf("autotz: testrun is on\n");
        if (test_type >= 0 && test_type <= 14) {
            inputlat = preset_loc[test_type][0];
            inputlong = preset_loc[test_type][1];
        }
    }

    if (debug) {
        printf("autotz: intput: lat: %.3f  long: %.3f\n", inputlat, inputlong);
    }

    search_city_table(inputlat, inputlong);

    return 0;
}
