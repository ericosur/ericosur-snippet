#ifndef MYCONTROLLER_H
#define MYCONTROLLER_H

#include <QObject>
#include <QThread>
#include <QTimer>

class Worker : public QObject
{
    Q_OBJECT
public:
    Worker(const QString& s);
    ~Worker() {}

    QString getResult() const {
        return m_wout;
    }

private:
    QString m_win;
    QString m_wout;

signals:
    void finished();
    void workError(const QString&);
    //void workProgress(int);

private slots:
    void doHardWork();
};  // class Worker


class MyController : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QString input READ getInput WRITE setInput)
    Q_PROPERTY(QString result READ getResult WRITE setResult NOTIFY resultChanged)

public:
    MyController(QObject *parent = 0);
    ~MyController();

    QString getInput() const;
    void setInput(const QString& s);
    QString getResult() const;
    void setResult(const QString& s);

    Q_INVOKABLE bool invokeWork();

protected:
    //void doHardWork();

signals:
    void resultChanged();

public slots:
    void onFinished();
    //void onProgress(int);
    void errString(const QString&);

private:
    QString m_input;
    QString m_result;
    QString m_error;

    QThread *m_thread;
    Worker *m_worker;
    QTimer *m_timer;
};

#endif // MYCONTROLLER_H
