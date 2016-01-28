/// file: barcontrol.cpp

#include "barcontrol.h"

#include <QDebug>

BarControl::BarControl()
    : m_count(0)
{
    m_timer = new QTimer(this);
    connect(m_timer, SIGNAL(timeout()), this, SLOT(onTimeout()));

    m_timer->start(750);

}

void BarControl::onStart()
{
    qDebug() << "onStart()";
}

void BarControl::onFinish()
{
    qDebug() << "onFinish";
}

void BarControl::onTimeout()
{
    qDebug() << "onTimeout:" << m_count;
    m_count ++;

    if (m_count > 5) {
        qDebug() << "emit sigClose";
        m_timer->stop();
        emit sigClose();
        emit sigAppQuit();
    }
}
