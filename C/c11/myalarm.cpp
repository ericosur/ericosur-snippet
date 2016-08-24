#include <iostream>
#include <unistd.h>
#include <signal.h>

using namespace std;

void my_alarm_handler(int a)
{
    cerr<<"my_alarm_handler"<<endl;
    alarm(2);//重新設定
}

int main()
{
    signal( SIGALRM, my_alarm_handler );
    alarm(1);

    while(1){}

    return 0;
}
