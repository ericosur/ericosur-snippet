#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QProcess>
#include <QDebug>
#include <QTextCodec>
#include <QFileInfo>
#include <QFileDialog>
#include <QFontDatabase>
#include <QDateTime>
#include <QLocale>
#include <QRegularExpression>
#include <QDir>

#ifdef Q_OS_WIN
#define DEFAULT_CONFIG_PATH "d:/src/testtool.conf"
#else
#define DEFAULT_CONFIG_PATH "./testtool.conf"
#endif
#define DEFAULT_BUFFER_SIZE 2048
#define VERSION "testtool v0.6"
#define TEST_STRING "1234567890123456789012345678901234567890123456789012345678901234567890"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    m_conf(NULL),
    m_process(NULL)
{
    ui->setupUi(this);

    QPalette p = ui->textEdit->palette();
    p.setColor(QPalette::Base, QColor(9, 9, 9));
    // background color for TextEdit
    ui->textEdit->setPalette(p);
    // text color for TextEdit
    ui->textEdit->setTextColor(QColor(255,255,255));

    initButtonGroups();
    signalMapperCategory = new QSignalMapper(this);
    signalMapperFunction = new QSignalMapper(this);
    initActionsConnections();

    m_category = 0;
    m_function = 0;
    m_stdout = "";
    m_stderr = "";
    m_currentTotalFunction = 0;

    m_fixedfont = QFontDatabase::systemFont(QFontDatabase::FixedFont);
    ui->textEdit->setCurrentFont(m_fixedfont);
    addline(m_fixedfont.toString());
    showCurrentTime();

    loadConfig(DEFAULT_CONFIG_PATH);
    //testLocal();
    //testSplit();
    testTime();

    addline(QDir::currentPath());
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::showCurrentTime()
{
    addline( QDateTime::currentDateTime().toString() );
    addline( QDateTime::currentDateTimeUtc().toString() );
}

void MainWindow::loadConfig(const QString& conf_path)
{
    if ( QFileInfo::exists(conf_path) ) {
        QTextCodec *codec = QTextCodec::codecForName("UTF-8");
        m_conf = new QSettings(conf_path, QSettings::IniFormat);
        m_conf->setIniCodec(codec);
        addline("config loaded from: " + conf_path);
        m_configpath = conf_path;
        initCategory();
        ui->textEdit->setReadOnly(true);
    } else {
        addline("config not exists at: " + conf_path);
    }
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
    INITCATEGORYBTN(5);
    INITCATEGORYBTN(6);
    INITCATEGORYBTN(7);
    INITCATEGORYBTN(8);
    INITCATEGORYBTN(9);
    INITCATEGORYBTN(10);
    INITCATEGORYBTN(11);
    INITCATEGORYBTN(12);
    INITCATEGORYBTN(13);
    INITCATEGORYBTN(14);
    INITCATEGORYBTN(15);

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

    // other actions
    //connect(ui->actionClear, SIGNAL(triggered()), this, SLOT(clearTextArea()));
    //connect(ui->actionQuit, SIGNAL(triggered()), this, SLOT(close()));
    //connect(ui->actionLoadConfig, SIGNAL(triggered()), this, SLOT(selectIniFile()));
    //connect(ui->lineEdit, SIGNAL(returnPressed()), this, SLOT(runLineCommand()));

    connect(ui->btnTerminate, SIGNAL(clicked(bool)), this, SLOT(slotTerminate()));
    connect(ui->btnInfo, SIGNAL(clicked(bool)), this, SLOT(slotInfo()));
    connect(ui->btnAbout, SIGNAL(clicked(bool)), this, SLOT(slotAbout()));
    connect(ui->btnClear, SIGNAL(clicked(bool)), this, SLOT(clearTextArea()));
    connect(ui->btnQuit, SIGNAL(clicked(bool)), this, SLOT(close()));
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
    m_currentTotalFunction = t;
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
            btnFunctionGroup[i]->setText( "" );
            btnFunctionGroup[i]->setEnabled(false);
        }
    }
    m_conf->endGroup();
}

void MainWindow::setAllFuncButtons(bool onOff)
{
    for (int i=0; i<m_currentTotalFunction; i++) {
        btnFunctionGroup[i]->setEnabled(onOff);
    }
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
    m_conf->endGroup();

    if (cmd != "") {
        addline("exec: " + cmd);
        setAllFuncButtons(false);
        runCommand(cmd);
    }
}

QString MainWindow::composeString(const QString s, int i)
{
    QString res;
    res = s + QString::number(i);
    return res;
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
            //ui->cbxCategory->addItem( s );
        }
        //qDebug() << m_conf->value(s.number(i)).toString();
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

void MainWindow::runLineCommand()
{
//    QString cmd = ui->lineEdit->text();
//    if (cmd != "") {
//        addline(cmd);
//        runCommand(cmd);
//    }
}

void MainWindow::selectIniFile()
{
    qDebug() << "selectIniFile()";
    QString fileName = QFileDialog::getOpenFileName(this,
        tr("Select Config File"), "./", tr("Config Files (*.ini *.conf)"));
    //addline("select file: " + fileName);
    loadConfig(fileName);
}

void MainWindow::keyPressEvent(QKeyEvent* e)
{
    addline("key(): " + QString::number(e->key(), 16));
    addline("nativescancode(): " + QString::number(e->nativeScanCode(), 16));
    addline("text(): "+ e->text());
}

void MainWindow::runCommand(const QString& cmd)
{
    m_process = new QProcess(this);

    connect(m_process, SIGNAL(started()), this, SLOT(slotStarted()));
    connect(m_process, SIGNAL(finished(int)), this, SLOT(slotFinished(int)));
    connect(m_process, SIGNAL(readyReadStandardOutput()), this, SLOT(slotReadStdout()));
    connect(m_process, SIGNAL(readyReadStandardError()), this, SLOT(slotReadStderr()));
    connect(m_process, SIGNAL(error(QProcess::ProcessError)), this, SLOT(slotError(QProcess::ProcessError)));
    connect(m_process, SIGNAL(stateChanged(QProcess::ProcessState)), this, SLOT(slotState(QProcess::ProcessState)));

    connect(this, SIGNAL(sigRequestTerminated()), m_process, SLOT(terminate()));
    connect(this, SIGNAL(sigCleanUp()), this, SLOT(slotCleanUp()));

#ifndef Q_OS_WIN
    QString append_cmd = QString("/bin/bash -c \"") + cmd + QString("\"");
#else
    QString append_cmd = QString("\"") + cmd + QString("\"");
#endif
    m_process->start(append_cmd);
    ui->btnTerminate->setEnabled(true);
    ui->btnInfo->setEnabled(true);
    //m_process->waitForFinished(-1); // will wait forever until finished
}

void MainWindow::slotStarted()
{
    //qDebug() << "slotStarted()";
}

void MainWindow::slotFinished(int i)
{
    //qDebug() << "slotFinished(): " << i;
    m_exitcode = i;

    disconnect(m_process, SIGNAL(started()), 0, 0);
    disconnect(m_process, SIGNAL(finished(int)), 0, 0);
    disconnect(m_process, SIGNAL(readyReadStandardOutput()), 0, 0);
    disconnect(m_process, SIGNAL(readyReadStandardError()), 0, 0);

    //addline(m_stdout);
    if (m_exitcode) {
        addline("Finished(): exit code != 0, exitcode = " + QString::number(m_exitcode));
        //addline(m_stderr);
    }

    //m_stdout = "";
    //m_stderr = "";
//    if (m_process) {
//        delete m_process;
//        m_process = NULL;
//    }

    emit sigCleanUp();
}

void MainWindow::slotCleanUp()
{
    ui->btnTerminate->setEnabled(false);
    ui->btnInfo->setEnabled(false);

    setAllFuncButtons(true);
}

void MainWindow::slotReadStdout()
{
    //qDebug() << "slotReadStdout";
    QString output = m_process->readAllStandardOutput();
    addline(output);
    //rasmus test
    testParse(output);
}

void MainWindow::slotReadStderr()
{
    //qDebug() << "slotReadStderr";
    addline(m_process->readAllStandardError());
}

void MainWindow::slotError(QProcess::ProcessError e)
{
    switch (e) {
    case QProcess::FailedToStart:
        break;
    case QProcess::Crashed:
        break;
    case QProcess::Timedout:
        break;
    case QProcess::WriteError:
        break;
    case QProcess::ReadError:
        break;
    case QProcess::UnknownError:
        break;
    }
}

void MainWindow::slotState(QProcess::ProcessState s)
{
    switch (s) {
    case QProcess::NotRunning:
        //qDebug() << "not running...";
        setAllFuncButtons(true);
        break;
    case QProcess::Starting:
        //qDebug() << "starting...";
        break;
    case QProcess::Running:
        //qDebug() << "running...";
        setAllFuncButtons(false);
        break;
    }
}

void MainWindow::slotTerminate()
{
    if (m_process) {
        addline("terminate clicked");
        emit sigRequestTerminated();
    }
}

void MainWindow::slotInfo()
{
    //addline("info clicked");
    QString str;
    if (m_process) {
        str = QString("pid: ") + QString::number(m_process->processId());
        addline(str);
    }
}

void MainWindow::slotAbout()
{
    addline(VERSION);
    QString build_datetime = QString("built at: ") + QString(__DATE__) + " " + QString(__TIME__);
    addline(build_datetime);
    addline(QString("config: " + m_configpath));
    addline(TEST_STRING);
}

void MainWindow::testLocale()
{

    //qDebug() << "test()";
    QLocale en = QLocale(QLocale::English, QLocale::UnitedKingdom);
    addline( en.dateTimeFormat(QLocale::ShortFormat) );
    addline( QDateTime::currentDateTime().toString(en.dateTimeFormat(QLocale::ShortFormat)) );

    QLocale us = QLocale(QLocale::English, QLocale::UnitedStates);
    addline( QDateTime::currentDateTime().toString(us.dateTimeFormat(QLocale::ShortFormat)) );

    QLocale pt = QLocale(QLocale::Portuguese, QLocale::Brazil);
    //addline( pt.dateTimeFormat() );
    addline( QDateTime::currentDateTime().toString(pt.dateTimeFormat(QLocale::ShortFormat)) );
}

void MainWindow::testParse(const QString& str)
{
#if 1
    QRegularExpression re("(\\d+\\.\\d+\\.\\d+\\.\\d+)");
    QRegularExpressionMatchIterator i = re.globalMatch(str);
    qDebug() << "str:" << str;
    //QStringList words;
    while (i.hasNext()) {
        QRegularExpressionMatch match = i.next();
        QString word1 = match.captured(1);
        //words << word;
        qDebug() << "word1:" << word1;
    }
#endif
}

QList<QString> MainWindow::testSplit()
{
    //QRegularExpression re("|");
    QString input = "mp3|mp4|mpg|wav|avi";
    QStringList filterlist = input.split("|");
    QList<QString> result;

    for (int i = 0; i < filterlist.size(); ++i) {
        result.append(filterlist.at(i));
        addline(filterlist.at(i));
    }
    return result;
}

void MainWindow::testTime()
{
    QDateTime dt = QDateTime::currentDateTime();
    addline( QString("time_t: ") + QString::number(dt.toTime_t()) );
}
