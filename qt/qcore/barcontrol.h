#ifndef BARCONTROL_H
#define BARCONTROL_H

#include <QObject>
#include <QTimer>

class BarControl : public QObject
{
    Q_OBJECT

public:
    BarControl();

public slots:
    void onStart();
    void onFinish();
    void onTimeout();

signals:
    void sigClose();
    void sigAppQuit();

private:
    int m_count;
    QTimer *m_timer;
};

#endif // BARCONTROL_H
