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
    MyController();
    ~MyController();

    QString getInput() const;
    void setInput(const QString& s);
    QString getResult() const;
    void setResult(const QString& s);

    Q_INVOKABLE bool invokeWork();
    Q_INVOKABLE void finish();

protected:
    //void doHardWork();

signals:
    void startWork();
    void resultChanged();
    void issueCleanup();

public slots:
    void onFinishWork();
    void onNotified(QObject* obj=0);
    void onFinished();

private:
    QString m_input;
    QString m_result;

    QThread *m_thread;
    Worker *m_worker;
};

#endif // MYCONTROLLER_H
