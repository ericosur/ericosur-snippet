#ifndef __RADIO_CONTROL_H__
#define __RADIO_CONTROL_H__

#include <QObject>
#include <QString>
#include <QThread>
#include <QDebug>

//namespace tef6638 {
#include "tef6638_radio.h"
//}

class Worker : public QObject
{
    Q_OBJECT
public:
    Worker(int);
    ~Worker() {}

    uint getResult() const {
        return m_wout;
    }

    void setGoup(int upDown) {
        m_isGoup = upDown;  // 1: seekUp, 0: seekDown
    }

    void setIsBusy(bool i)
    {
        m_isBusy = i;
    }

    bool getIsBusy()
    {
        return m_isBusy;
    }

private:
    int m_isGoup;
    uint m_wout;

    bool m_isBusy;

signals:
    void finished();
    //void workProgress(int);

private slots:
    void seek();
    void _setFrequency(quint16);
};  // class Worker


class RadioControl : public QObject
{
    Q_OBJECT

    Q_PROPERTY(bool enabled READ getEnabled)
    Q_PROPERTY(QString freqstr READ getFreqstr)
    Q_PROPERTY(uint freqval READ getFreqval)
    Q_PROPERTY(QString radiotype READ getRadiotype WRITE setRadiotype)
    Q_PROPERTY(QString Maxfreq READ getMaxfreq NOTIFY maxFreqChanged  )
    Q_PROPERTY(QString Minfreq READ getMinfreq NOTIFY minFreqChanged )

public:
    RadioControl();
    ~RadioControl();

    bool getEnabled() const {
        return m_enabled;
    }
/*
    void setEnalbed(bool onOff) {
        m_enabled = onOff;
    }
*/
    QString getFreqstr() const;
    uint getFreqval() const;

    QString getMaxfreq() const {
        return m_maxfreq;
    }
    QString getMinfreq() const {
        return m_minfreq;
    }
    QString getRadiotype() const {
        return m_radiotype;
    }
    void setRadiotype(QString s);

    // enable radio
    Q_INVOKABLE void enableRadio(bool onOff);
    Q_INVOKABLE void disableRadio();
    Q_INVOKABLE void readRadioInfo();
    Q_INVOKABLE void seekRadioUp();
    Q_INVOKABLE void seekRadioDown();
    Q_INVOKABLE void setFreqval(uint, bool);
    Q_INVOKABLE void finish();
    Q_INVOKABLE void dump_radio_info();
    Q_INVOKABLE QString fm_val2str(uint);
    Q_INVOKABLE QString am_val2str(uint);
    Q_INVOKABLE void setRadioVol(quint16 vol);

protected:

signals:
    void startSeek();
    void setFreq(quint16);
    void resultChanged();
    void issueCleanup();

    void minFreqChanged();
    void maxFreqChanged();

    void started();

public slots:
    void onFinishWork();
    void onFinished();

    void getStarted();

private:
    Radio_InfoDef *m_info;
    bool m_enabled;
    QString m_freqstr;
    uint m_freqval;
    QString m_radiotype;
    QString m_maxfreq;
    QString m_minfreq;
    //QString m_step;
    uint m_result;

    Worker *m_worker;
    QThread *m_thread;
};

#endif // __RADIO_CONTROL_H__
