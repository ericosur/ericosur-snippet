#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QLocale>
#include <QDebug>
#include <QProcessEnvironment>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    test();
    test_getenv();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::setLabel1(const QString& s)
{
    ui->label_1->setText(s);
}
void MainWindow::setLabel2(const QString& s)
{
    ui->label_2->setText(s);
}
void MainWindow::setLabel3(const QString& s)
{
    ui->label_3->setText(s);
}

void MainWindow::test()
{
    QLocale::setDefault(QLocale(QLocale::Hebrew, QLocale::Israel));
    QLocale hebrew; // Constructs a default QLocale
    QString s1 = hebrew.toString(15714.3, 'e');

    setLabel1(s1);

    bool ok;
    double d;

    QLocale::setDefault(QLocale::C);
    d = QString("1234,56").toDouble(&ok);   // ok == false
    d = QString("1234.56").toDouble(&ok);   // ok == true, d == 1234.56

    QLocale::setDefault(QLocale::German);
    d = QString("1234,56").toDouble(&ok);   // ok == true, d == 1234.56
    d = QString("1234.56").toDouble(&ok);   // ok == true, d == 1234.56

    QLocale::setDefault(QLocale(QLocale::English, QLocale::UnitedStates));
    QString str = QString("%1 %L2 %L3").
            arg(12345).arg(12345).arg(12345, 0, 16);
    // str == "12345 12,345 3039"
    setLabel2(str);
}

void MainWindow::test_getenv()
{
    QString path = QProcessEnvironment::systemEnvironment().value("PATH", "");
    setLabel3(path);
}
