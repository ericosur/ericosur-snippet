//#include <QCoreApplication>

int demoCapture();
int demoTest();

int main(int argc, char *argv[])
{
    //QCoreApplication a(argc, argv);
    //return a.exec();

    //demoCapture();
    if ( demoTest() == -1 ) {
        return -1;
    }

    //a.quit();

    return 0;
}
