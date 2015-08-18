#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    test();
}

MainWindow::~MainWindow()
{

}

void MainWindow::test()
{
    QTextCodec *codec = QTextCodec::codecForName("UTF-8");
    QSettings qq("/Users/ericosur/pega.rasmus.ini", QSettings::IniFormat);
    qq.setIniCodec(codec);

    qq.setValue("editor/wrapMargin", 68);
    qq.setValue("%U4E2D%U6587", "chinese characters");
    qq.setValue("地點/地址", "台北市北投區承德路7段400號");
}
