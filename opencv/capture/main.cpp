#include <QCoreApplication>

int demoCapture();
int demoTest();

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    //a.exec();

    //demoCapture();
    demoTest();

    //a.quit();

    return a.exec();
}
