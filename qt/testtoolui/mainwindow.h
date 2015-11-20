#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QSignalMapper>
#include <QPushButton>
#include <QSettings>
#include <QKeyEvent>
#include <QProcess>

#include "jobcontrol.h"

namespace Ui {
class MainWindow;
}

const int MAX_CATEGORY = 5;
const int MAX_FUNCTION = 10;

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

    void keyPressEvent(QKeyEvent* e);

private slots:
    void categoryClicked(int i);
    void functionClicked(int i);
    void clearTextArea();
    void runLineCommand();
    void selectIniFile();
    void slotFinished(int i);
    void slotReadStdout();
    void slotReadStderr();

private:
    void initButtonGroups();
    void initActionsConnections();
    void loadConfig(const QString& conf_path);
    QString composeString(const QString s, int i);
    void test();
    void initCategory();
    void runCommand(const QString& s);
    void addline(const QString& s);

private:
    Ui::MainWindow *ui;
    // ini config object
    QSettings *m_conf;
    // category buttons
    QSignalMapper *signalMapperCategory;
    QPushButton *btnCategoryGroup[MAX_CATEGORY];
    int m_category;
    // function buttons
    QSignalMapper *signalMapperFunction;
    QPushButton *btnFunctionGroup[MAX_FUNCTION];
    int m_function;

    JobControl *m_job;
};

#endif // MAINWINDOW_H
