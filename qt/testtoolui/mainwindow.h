#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QSignalMapper>
#include <QPushButton>
#include <QSettings>
#include <QKeyEvent>
#include <QProcess>

namespace Ui {
class MainWindow;
}

const int MAX_CATEGORY = 16;
const int MAX_FUNCTION = 8;

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

    void keyPressEvent(QKeyEvent* e);
    void runCommand(const QString& cmd);

private slots:
    void categoryClicked(int i);
    void functionClicked(int i);
    void clearTextArea();
    void selectIniFile();
    void runLineCommand();

    void slotStarted();
    void slotFinished(int i);
    void slotReadStdout();
    void slotReadStderr();
    void slotError(QProcess::ProcessError e);
    void slotState(QProcess::ProcessState s);

    void slotTerminate();
    void slotInfo();
    void slotCleanUp();
    void slotAbout();

signals:
    void sigRequestTerminated();
    void sigCleanUp();

private:
    void initButtonGroups();
    void initActionsConnections();
    void loadConfig(const QString& conf_path);
    QString composeString(const QString s, int i);
    void initCategory();
    void addline(const QString& s);
    void setAllFuncButtons(bool onOff);
    void showCurrentTime();
    void testLocale();
    void testParse(const QString& s);
    //void testSplit();
    QList<QString> testSplit();
    void testTime();

private:
    Ui::MainWindow *ui;
    // ini config object
    QSettings *m_conf;
    QString m_configpath;
    // category buttons
    QSignalMapper *signalMapperCategory;
    QPushButton *btnCategoryGroup[MAX_CATEGORY];
    int m_category;
    // function buttons
    QSignalMapper *signalMapperFunction;
    QPushButton *btnFunctionGroup[MAX_FUNCTION];
    int m_function;
    int m_currentTotalFunction;

    QProcess *m_process;
    QString m_stdout;
    QString m_stderr;
    int m_exitcode;

    QFont m_fixedfont;
};

#endif // MAINWINDOW_H
