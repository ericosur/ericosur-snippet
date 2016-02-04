#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTimer>
#include <QSettings>
#include <QElapsedTimer>

#include "mythreads.h"

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = 0);
    ~MainWindow();

    void init_settings();

signals:

public slots:
    void onStarted();
    void onFinished1();
    void onFinished2();
    void onFinished3();
    void onTimeout();

private:
    int m_threadcount;
    int m_counter;
    QTimer *m_timer;
    QSettings *m_setting;
    QElapsedTimer *m_epoch;

    ThreadFoo *foo1;
    ThreadFoo *foo2;
    ThreadFoo *foo3;
};

#endif // MAINWINDOW_H
