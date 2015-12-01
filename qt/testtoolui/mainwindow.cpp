#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QProcess>
#include <QDebug>
#include <QTextCodec>
#include <QFileInfo>
#include <QFileDialog>

#define DEFAULT_CONFIG_PATH "./test-tool.conf"
#define DEFAULT_BUFFER_SIZE 2048
#define VERSION "testtool v0.3"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow),
    m_conf(NULL),
    m_process(NULL)
{
    ui->setupUi(this);

    initButtonGroups();
    signalMapperCategory = new QSignalMapper(this);
    signalMapperFunction = new QSignalMapper(this);
    initActionsConnections();

    m_category = 0;
    m_function = 0;
    m_stdout = "";
    m_stderr = "";

    loadConfig(DEFAULT_CONFIG_PATH);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::loadConfig(const QString& conf_path)
{
    if ( QFileInfo::exists(conf_path) ) {
        QTextCodec *codec = QTextCodec::codecForName("UTF-8");
        m_conf = new QSettings(conf_path, QSettings::IniFormat);
        m_conf->setIniCodec(codec);
        addline("config loaded from: " + conf_path);

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

    // other actions
    connect(ui->actionClear, SIGNAL(triggered()), this, SLOT(clearTextArea()));
    connect(ui->actionQuit, SIGNAL(triggered()), this, SLOT(close()));
    connect(ui->actionLoadConfig, SIGNAL(triggered()), this, SLOT(selectIniFile()));
    connect(ui->lineEdit, SIGNAL(returnPressed()), this, SLOT(runLineCommand()));

    connect(ui->btnTerminate, SIGNAL(clicked(bool)), this, SLOT(slotTerminate()));
    connect(ui->btnInfo, SIGNAL(clicked(bool)), this, SLOT(slotInfo()));
    connect(ui->btnAbout, SIGNAL(clicked(bool)), this, SLOT(slotAbout()));
    connect(ui->btnClear, SIGNAL(clicked(bool)), this, SLOT(clearTextArea()));
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

void MainWindow::setAllFuncButtons(bool onOff)
{
    for (int i=0; i<MAX_FUNCTION; i++) {
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
    addline("exec: " + cmd);
    m_conf->endGroup();

    if (cmd != "") {
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
    QString cmd = ui->lineEdit->text();
    if (cmd != "") {
        addline(cmd);
        runCommand(cmd);
    }
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

    connect(m_process, SIGNAL(finished(int)), this, SLOT(slotFinished(int)));
    connect(m_process, SIGNAL(readyReadStandardOutput()), this, SLOT(slotReadStdout()));
    connect(m_process, SIGNAL(readyReadStandardError()), this, SLOT(slotReadStderr()));

    connect(this, SIGNAL(sigStdoutChanged()), this, SLOT(slotUpdateUi()));
    connect(this, SIGNAL(sigStderrChanged()), this, SLOT(slotUpdateUi()));
    connect(this, SIGNAL(sigRequestTerminated()), m_process, SLOT(terminate()));
    connect(this, SIGNAL(sigCleanUp()), this, SLOT(slotCleanUp()));

    m_process->start(cmd);
    ui->btnTerminate->setEnabled(true);
    ui->btnInfo->setEnabled(true);
    //m_process->waitForFinished(-1); // will wait forever until finished
}

void MainWindow::slotFinished(int i)
{
    //qDebug() << "slotFinished(): " << i;
    m_exitcode = i;

    disconnect(m_process, SIGNAL(finished(int)), 0, 0);
    disconnect(m_process, SIGNAL(readyReadStandardOutput()), 0, 0);
    disconnect(m_process, SIGNAL(readyReadStandardError()), 0, 0);

    addline(m_stdout);
    if (m_exitcode) {
        addline("Finished(): exit code != 0, exitcode = " + QString::number(m_exitcode));
        addline(m_stderr);
    }

    m_stdout = "";
    m_stderr = "";
//    if (m_process) {
//        delete m_process;
//        m_process = NULL;
//    }

    emit sigCleanUp();
}

void MainWindow::slotCleanUp()
{
//    if (m_process) {
//        delete m_process;
//        m_process = NULL;
//    }
    ui->btnTerminate->setEnabled(false);
    ui->btnInfo->setEnabled(false);

    setAllFuncButtons(true);
}

void MainWindow::slotReadStdout()
{
    //qDebug() << "slotReadStdout";
#if 0
    // use readLine() to read from stdout
    char stdbuf[DEFAULT_BUFFER_SIZE];
    qint64 len = m_process->readLine(stdbuf, DEFAULT_BUFFER_SIZE);
    if (len != -1) {
        // the line is available in buf
        m_stdout = QString::fromUtf8(stdbuf);
    }
#else
    // use QByteArray to read stdout
    QByteArray arr = m_process->read(DEFAULT_BUFFER_SIZE);
    // the line is available in buf

    //QByteArray arr = m_process->readAllStandardOutput();
    m_stdout = QString::fromUtf8(arr);
#endif

    emit sigStdoutChanged();
}

void MainWindow::slotReadStderr()
{
    //qDebug() << "slotReadStderr";
    QByteArray arr = m_process->read(DEFAULT_BUFFER_SIZE);
    // the line is available in buf
    //m_stderr = QString::fromUtf8(arr);
    m_stderr = m_process->readAllStandardError();
    emit sigStderrChanged();
}

void MainWindow::slotUpdateUi()
{
    //qDebug() << "slotUpdateUi()";
    //clearTextArea();
    addline(m_stdout);
    //addline(m_stderr);
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
}
