#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QProcess>
#include <QDebug>
#include <QTextCodec>

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

    QTextCodec *codec = QTextCodec::codecForName("UTF-8");
    m_conf = new QSettings("/home/rasmus/test-tool.conf", QSettings::IniFormat);
    m_conf->setIniCodec(codec);

    initCategory();
    ui->textEdit->setReadOnly(true);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::initButtonGroups()
{
#define INITCATEGORYBTN(n)    \
    btnCategoryGroup[n] = ui->btnCategory##n ;  \
    btnCategoryGroup[n]->setText(composeString("cat", n)); \
    btnCategoryGroup[n]->setEnabled(false);

    //btnCategoryGroup[n]->setVisible(false);

    INITCATEGORYBTN(0);
    INITCATEGORYBTN(1);
    INITCATEGORYBTN(2);
    INITCATEGORYBTN(3);
    INITCATEGORYBTN(4);

#undef INITCATEGORYBTN

#define INITFUNCTIONBTN(n)    \
    btnFunctionGroup[n] = ui->btnFunc##n ; \
    btnFunctionGroup[n]->setText(composeString("func", n)); \
    btnFunctionGroup[n]->setEnabled(false);

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

    connect(ui->actionClear, SIGNAL(triggered()), this, SLOT(clearTextArea()));
    connect(ui->actionQuit, SIGNAL(triggered()), this, SLOT(close()));
}

// this SLOT will know which btnCategory## is clicked
void MainWindow::categoryClicked(int i)
{
    m_category = i;
    //qDebug() << "execCategory() " << m_category;
    QString cat_name = m_conf->value(QString::number(i)).toString();
    m_conf->beginGroup(cat_name);
    int t = m_conf->value("total", 0).toInt();
    //qDebug() << "t: " << t;
    for (int i=0; i<MAX_FUNCTION; i++) {
        if (i<t) {
            QString but_name = QString("button") + QString::number(i);
            QString but_text = m_conf->value(but_name, "").toString();
            if (but_text == "") {
                btnFunctionGroup[i]->setText( "" );
                btnFunctionGroup[i]->setEnabled(false);
            } else {
                btnFunctionGroup[i]->setText( but_text );
                btnFunctionGroup[i]->setEnabled(true);
            }
        } else {
            btnFunctionGroup[i]->setText( "n/a" );
            btnFunctionGroup[i]->setEnabled(false);
        }
    }
    m_conf->endGroup();
}

// this SLOT will know which btnFunc## is clicked
void MainWindow::functionClicked(int i)
{
    m_function = i;
    //qDebug() << "execFunction() " << m_function << " of category " << m_category;
    QString cat_name = m_conf->value(QString::number(m_category),"").toString();
    if (cat_name == "") {
        qDebug() << "cat_name is empty, exit...";
        return;
    }
    //qDebug() << "cat_name: " << cat_name;
    m_conf->beginGroup(cat_name);
    QString act_name = "action" + QString::number(m_function);
    QString act_value = m_conf->value(act_name, "").toString();
    QString res, cmd;
    res = "cat_name: " + cat_name + " action: " + act_name + " act_value: " + act_value;
    cmd = act_value;
    addline(cmd);
    m_conf->endGroup();

    if (cmd != "") {
        runCommand(cmd);
    }
}

QString MainWindow::composeString(const QString s, int i)
{
    QString res;
    res = s + QString::number(i);
    return res;
}

void MainWindow::test()
{

}

void MainWindow::initCategory()
{
    QString s;
    int total = m_conf->value("total", MAX_CATEGORY).toInt();
    //qDebug() << "total: " << total;
    for (int i=0; i<total; i++) {
        s = m_conf->value(s.number(i)).toString();
        //qDebug() << "s: " << s;

        if (i < MAX_CATEGORY) {
            btnCategoryGroup[i]->setText( s );
            btnCategoryGroup[i]->setEnabled(true);
        } else {
            ui->cbxCategory->addItem( s );
        }
        //qDebug() << m_conf->value(s.number(i)).toString();
    }
}

void MainWindow::runCommand(const QString& cmd)
{
    QProcess process;
    process.start(cmd);
    process.waitForFinished(-1); // will wait forever until finished

    QString stdout = process.readAllStandardOutput();
    QString stderr = process.readAllStandardError();

    //qDebug() << "stdout: " << stdout;
    //qDebug() << "stderr: " << stderr;

    addline("========== stdout ==========");
    addline(stdout);
    if (stderr != "") {
        addline("========== stderr ==========");
        addline(stderr);
    }
}

void MainWindow::addline(const QString &s)
{
    ui->textEdit->append(s);
}

void MainWindow::clearTextArea()
{
    ui->textEdit->clear();
}
