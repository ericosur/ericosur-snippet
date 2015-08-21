#ifndef COLORMARKER_H
#define COLORMARKER_H

#include <QObject>
#include <QColor>
#include <QDebug>
#include <QThread>

#include <iostream>

class ColorMaker : public QObject
{
    Q_OBJECT
    Q_ENUMS(GenerateAlgorithm)
    Q_PROPERTY(QColor color READ color WRITE setColor NOTIFY colorChanged)
    Q_PROPERTY(QColor timeColor READ timeColor)

public:
    ColorMaker(QObject *parent = 0);
    ~ColorMaker();

    enum GenerateAlgorithm{
        RandomRGB,
        RandomRed,
        RandomGreen,
        RandomBlue,
        LinearIncrease
    };

    QColor color() const;
    void setColor(const QColor & color);
    QColor timeColor() const;

    Q_INVOKABLE GenerateAlgorithm algorithm() const;
    Q_INVOKABLE void setAlgorithm(GenerateAlgorithm algorithm);
    Q_INVOKABLE QString getData(QString qStr);

signals:
    void colorChanged(const QColor & color);
    void currentTime(const QString &strTime);
    void testSignal();

public slots:
    void start();
    void stop();
    bool testSlot();

protected:
    void timerEvent(QTimerEvent *e);

private:
    GenerateAlgorithm m_algorithm;
    QColor m_currentColor;
    int m_nColorTimer;
};

#endif // COLORMARKER_H
