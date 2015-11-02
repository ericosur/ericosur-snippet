#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QSignalMapper>
#include <QPushButton>
#include <QSettings>

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

private slots:
    void categoryClicked(int i);
    void functionClicked(int i);
    void clearTextArea();

private:
    void initButtonGroups();
    void initActionsConnections();
    QString composeString(const QString s, int i);
    void test();
    void initCategory();
    void runCommand(const QString& s);
    void addline(const QString& s);

private:
    Ui::MainWindow *ui;
    QSignalMapper *signalMapperCategory;
    QPushButton *btnCategoryGroup[MAX_CATEGORY];
    int m_category;

    QSignalMapper *signalMapperFunction;
    QPushButton *btnFunctionGroup[MAX_FUNCTION];
    int m_function;
    QSettings *m_conf;
};

#endif // MAINWINDOW_H
