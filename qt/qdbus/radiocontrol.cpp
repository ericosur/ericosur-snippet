#include "radiocontrol.h"

#include <QDebug>
#include <stdio.h>
#include <QCryptographicHash>

#include "tef6638_radio.h"

RadioControl::RadioControl() :
    m_enabled(false)
    , m_freqstr("")
    , m_freqval(0)
    , m_radiotype("")
    , m_maxfreq("")
    , m_minfreq("")
{
    m_info = new Radio_InfoDef;
    memset(m_info, 0, sizeof(Radio_InfoDef));

    m_worker = new Worker(1);
    m_thread = new QThread;
    m_worker->moveToThread( m_thread );

    // Init connection
    connect(this, SIGNAL(startSeek()), m_worker, SLOT(seek()));
    connect(m_worker, SIGNAL(finished()), this, SLOT(onFinishWork()));
    connect(this, SIGNAL(issueCleanup()), m_thread, SLOT(quit()));
    connect(m_thread, SIGNAL(finished()), this, SLOT(onFinished()) );
    connect( this, SIGNAL(setFreq(quint16)), m_worker, SLOT(_setFrequency(quint16)) );

    m_thread->start();
}

RadioControl::~RadioControl()
{
    delete m_info;
    delete m_worker;
    //delete m_thread;
    emit issueCleanup();
}

QString RadioControl::getFreqstr() const
{
    return m_freqstr;
}

uint RadioControl::getFreqval() const
{
    return m_freqval;
}

void RadioControl::setFreqval(uint v, bool isQueue )
{
    if( isQueue )
    {
        m_freqval = v;
        emit setFreq(v);
    }
    else
    {
        if( !(m_worker->getIsBusy()) )
        {
            m_freqval = v;
            emit setFreq(v);
        }
    }

}

// may set fm/FM
void RadioControl::setRadiotype(QString s) {
    QRegExp re("am");
    re.setCaseSensitivity(Qt::CaseInsensitive);
    if ( s.contains(re) ) {
        m_radiotype = "AM";
        setMode(3);
        qDebug() << "RadioControl::setRadioType()" << s;
    } else {
        m_radiotype = "FM";
        setMode(0);
        qDebug() << "RadioControl::setRadioType()" << s;
    }
    //qDebug() << "tef6638::setMode()";
}

void RadioControl::enableRadio(bool onOff)
{
    if (onOff) {
        qDebug() << "tef6638::enable() " << m_freqval;
        //setenv(“PULSE_PROP”, “media.role=video”, 1 );
        qputenv("PULSE_PROP", QByteArray("media.role=radio"));

        enable(m_freqval);
    } else {
        qDebug() << "tef6638::disable()";
        disable();
    }
}

void RadioControl::disableRadio()
{
    qDebug() << "tef6638::disable()";
    disable();
}

void RadioControl::readRadioInfo()
{
    radioInfo(m_info);
    m_enabled = (m_info->enable==1);
    m_freqval = m_info->current_freq;
    if (m_info->radio_band) {
        m_radiotype = "AM";
        m_freqstr = am_val2str(m_freqval);
        m_maxfreq = QString::number(m_info->BandInfo.AM_MaxFreq);
        m_minfreq = QString::number(m_info->BandInfo.AM_MinFreq);
    } else {
        m_radiotype = "FM";
        m_freqstr = fm_val2str(m_freqval);
        m_maxfreq = QString::number(m_info->BandInfo.FM_MaxFreq);
        m_minfreq = QString::number(m_info->BandInfo.FM_MinFreq);
    }

    emit minFreqChanged();
    emit maxFreqChanged();
}

void RadioControl::seekRadioUp()
{
    m_worker->setGoup(1);
    // call tef6638::seekUp(), it's blocking
    emit startSeek();
}

void RadioControl::seekRadioDown()
{
    m_worker->setGoup(0);
    // call tef6638::seekDown(), it's blocking
    emit startSeek();
}

void RadioControl::dump_radio_info()
{
    printf("onOff(%u), freq(%u), type(%u),\n",
        m_info->enable, m_info->current_freq, m_info->radio_band);
    printf("FM max(%u), min(%u), step(%u),\nAM max(%u), min(%u), step(%u)\n",
        m_info->BandInfo.FM_MaxFreq, m_info->BandInfo.FM_MinFreq,
        m_info->BandInfo.FM_SeekStep,
        m_info->BandInfo.AM_MaxFreq, m_info->BandInfo.AM_MinFreq,
        m_info->BandInfo.AM_SeekStep);
}

void RadioControl::finish()
{
    emit issueCleanup();
}

void RadioControl::onFinishWork()
{
    m_result = m_worker->getResult();
    m_freqval = m_result;

    //qDebug() << "RadioControl::onFinished()";
    qDebug() << "m_result: " << m_result;

    if (m_info->radio_band < 3) {
        // FM
        m_freqstr = fm_val2str(m_freqval);
    } else {
        // AM
        m_freqstr = am_val2str(m_freqval);
    }

    qDebug() << "emit resultChanged(), m_freqstr: " << m_freqstr;
    emit resultChanged();
}

void RadioControl::onFinished()
{
    //qDebug() << "Get signal 'Finished'.";
    exit(0);
}

QString RadioControl::fm_val2str(uint val)
{
    qDebug() << "val = " << val;
    // 10070 -> 100.7MHz
    QString ret = QString::number(val);
    ret.insert(ret.length()-2, QString("."));
    qDebug() << "fm_val2str()" << val << " -> " << ret;
    return ret;
}

QString RadioControl::am_val2str(uint val)
{
    // 1200 -> 1200kHz
    qDebug() << "am_val2str()" << val;
    return QString(val);
}

void RadioControl::setRadioVol(quint16 vol)
{
#ifdef USE_YOSETARGET
    qDebug() << "setVolumeGain()" << vol;
    setVolumeGain(vol);
#else
    (void)vol;
#endif
}
//////////////////////////////////////////////////////////////////////////////


Worker::Worker(int isGoup) :
    m_isGoup(isGoup),
    m_wout(0),
    m_isBusy(false)
{}

void Worker::_setFrequency(quint16 freq)
{
    setIsBusy( true );

    quint16 result = freq;
    enable(result);

    // read radio info again
    struct Radio_InfoDef info;
    radioInfo(&info);
    qDebug() << "current.freq: " << info.current_freq;

    m_wout = (uint)result;
    qDebug() << "m_wout: " << m_wout;
    qDebug() << "_setFrequency() finished, emit finished()";
    emit finished();

    //m_mutex.unlock();
    setIsBusy(false);
}

void Worker::seek()
{
    //qDebug() << "worker thread id: " << QThread::currentThreadId();
    //qDebug() << "doHardWork() start...";

    quint16 result = 0;
    if (m_isGoup) {
        qDebug() << "tef6638::seekUp()";
        result = seekUp();
    } else {
        qDebug() << "tef6638::seekDown()";
        result = seekDown();
    }

    // cannot believe return value of seekUp() / seekDown()
    qDebug() << "seek result: " << result;
    enable(result);

    // read radio info again
    struct Radio_InfoDef info;
    radioInfo(&info);
    qDebug() << "current.freq: " << info.current_freq;

    m_wout = (uint)result;
    qDebug() << "m_wout: " << m_wout;
    qDebug() << "seek() finished, emit finished()";
    emit finished();
}
