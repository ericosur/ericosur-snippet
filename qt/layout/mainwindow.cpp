#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QDebug>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    initButtonGroups();
    signalMapperCategory = new QSignalMapper(this);
    signalMapperFunction = new QSignalMapper(this);
    initActionsConnections();
    m_category = 0;
    m_function = 0;
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::initButtonGroups()
{
#define INITCATEGORYBTN(n)    \
    btnCategoryGroup[n] = ui->btnCategory##n ;  \
    btnCategoryGroup[n]->setText(composeString("category", n));

    INITCATEGORYBTN(0);
    INITCATEGORYBTN(1);
    INITCATEGORYBTN(2);
    INITCATEGORYBTN(3);
    INITCATEGORYBTN(4);

#undef INITCATEGORYBTN

#define INITFUNCTIONBTN(n)    \
    btnFunctionGroup[n] = ui->btnFunc##n ; \
    btnFunctionGroup[n]->setText(composeString("func", n));

    INITFUNCTIONBTN(0);
    INITFUNCTIONBTN(1);
    INITFUNCTIONBTN(2);
    INITFUNCTIONBTN(3);
    INITFUNCTIONBTN(4);
    INITFUNCTIONBTN(5);
    INITFUNCTIONBTN(6);
    INITFUNCTIONBTN(7);
    INITFUNCTIONBTN(8);
    INITFUNCTIONBTN(9);
#undef INITFUNCTIONBTN

}

void MainWindow::initActionsConnections()
{
    // for btnCategory##
    for (int i = 0; i < MAX_CATEGORY; ++i) {
        connect(btnCategoryGroup[i], SIGNAL(clicked()), signalMapperCategory, SLOT(map()));
        signalMapperCategory->setMapping(btnCategoryGroup[i], i);
    }
    connect(signalMapperCategory, SIGNAL(mapped(int)), this, SLOT(categoryClicked(int)));

    // for btnFunc##
    for (int i = 0; i < MAX_FUNCTION; ++i) {
        connect(btnFunctionGroup[i], SIGNAL(clicked()), signalMapperFunction, SLOT(map()));
        signalMapperFunction->setMapping(btnFunctionGroup[i], i);
    }
    connect(signalMapperFunction, SIGNAL(mapped(int)), this, SLOT(functionClicked(int)));

}

// this SLOT will know which btnCategory## is clicked
void MainWindow::categoryClicked(int i)
{
    m_category = i;
    qDebug() << "execCategory() " << i;
}

// this SLOT will know which btnFunc## is clicked
void MainWindow::functionClicked(int i)
{
    m_function = i;
    qDebug() << "execFunction() " << m_function << " of category " << m_category;
}

QString MainWindow::composeString(const QString s, int i)
{
    QString res;
    res = s + res.number(i);
    return res;
}
