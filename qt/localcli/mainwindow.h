#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

    void test();
    void test_getenv();

private:
    Ui::MainWindow *ui;

    void setLabel1(const QString& s);
    void setLabel2(const QString& s);
    void setLabel3(const QString& s);
};

#endif // MAINWINDOW_H
