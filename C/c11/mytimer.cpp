#include <iostream>
#include <sys/time.h>
#include <signal.h>
#include <unistd.h>

using namespace std;

void my_alarm_handler(int a)
{
    static int count = 0;
    cerr << "test: " << count << endl;
    count ++;
}


int main()
{
    struct itimerval t;
    t.it_interval.tv_usec = 750 * 1000;
    t.it_interval.tv_sec = 0;
    t.it_value.tv_usec = 500 * 1000;
    t.it_value.tv_sec = 0;

    if( setitimer( ITIMER_REAL, &t, NULL) < 0 ){
        cerr<<"settimer error."<<endl;
        return -1;
    }
    signal( SIGALRM, my_alarm_handler );

    while(true) {
        sleep(1);
        cerr << "after sleep 1..." << endl;
    }
    return 0;
}
