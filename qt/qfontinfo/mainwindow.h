#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

    void store_font(const QFont f) {
        m_font = f;
    }

private:
    Ui::MainWindow *ui;
    QFont m_font;

    void test();
};

#endif // MAINWINDOW_H
