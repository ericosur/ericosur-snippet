#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QString>


#include "simplenotify.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    void addline(const QString& s);

public slots:
    void gotMessage(const QString& s);
    void testNotify(bool b);
    void showStarted();
    void showFinished();
    void getNotified();

private:
    Ui::MainWindow *ui;
    SimpleNotify *m_sn;
};

#endif // MAINWINDOW_H
