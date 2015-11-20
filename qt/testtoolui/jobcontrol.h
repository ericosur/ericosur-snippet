#ifndef __Job_CONTROL_H__
#define __Job_CONTROL_H__

#include <QObject>
#include <QString>
#include <QThread>
#include <QDebug>
#include <QProcess>

class JobWorker : public QObject
{
    Q_OBJECT
public:
    JobWorker();
    ~JobWorker() {}

private:
    bool m_working;
    QProcess m_process;

signals:
    void sigJobFinished();
    void sigOutputChanged(const QByteArray& arr);

private slots:
    void doJobWork(const QString& cmd);
    void slotFinished(int exitCode);
    void slotReadStdout();
    void slotReadStderr();

protected:
    void endJobWork();
    void runCommand(const QString& cmd);

};  // class JobWorker



class JobControl : public QObject
{
    Q_OBJECT


public:
    JobControl();
    ~JobControl();


    void setCmd(const QString& cmd) {
        m_cmd = cmd;
    }
    QString getCmd() const {
        return m_cmd;
    }
    QByteArray getArray() const {
        return m_array;
    }
    // enable Job
    Q_INVOKABLE void startJob();
    Q_INVOKABLE void finishJob();

protected:

signals:
    void sigHasJob();
    void sigResultChanged();
    void sigIssueCleanup();

public slots:
    void onFinishWork();
    void onFinished();
    void onOutputChanged();

private:
    QString m_cmd;
    JobWorker *m_worker;
    QThread *m_thread;
    QByteArray m_array;
};

#endif // __Job_CONTROL_H__
