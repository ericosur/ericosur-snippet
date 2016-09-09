/** \file mynoise.cpp
**/

#include "mynoise.h"
#include <QString>
#include <QDebug>
#include <QRegularExpression>

#ifdef __cplusplus
extern "C" {
#endif

char myhint[80];

void completion(const char *buf, linenoiseCompletions *lc)
{
    MyNoise::getInstance()->add_completion(buf, lc);
}

char *hints(const char *buf, int *color, int *bold)
{
    char *p = NULL;
    p = MyNoise::getInstance()->add_hint(buf);
    if (p!=NULL) {
        *color = 36;
        *bold = 0;
        return p;
    }

    return NULL;

}
#ifdef __cplusplus
}   // extern "C"
#endif

#define HISTORY_FILE    "/tmp/noisehistory.txt"

MyNoise* MyNoise::_instance = NULL;
MyNoise* MyNoise::getInstance()
{
    if (_instance == NULL) {
        _instance = new MyNoise;
    }
    return _instance;
}

MyNoise::MyNoise()
{
}

void MyNoise::setup()
{
    /* Set the completion callback. This will be called every time the
     * user uses the <tab> key. */
    linenoiseSetCompletionCallback(completion);
    linenoiseSetHintsCallback(hints);

    /* Load history from file. The history file is just a plain text file
     * where entries are separated by newlines. */
    linenoiseHistoryLoad(HISTORY_FILE); /* Load the history at startup */

    connect(this, SIGNAL(sigCommand(QString)), ActionHandler::getInstance(), SLOT(sltHandleMsg(QString)));
}

void MyNoise::startcommandloop()
{
    char *line;
    int ret = 0;
    /* Now this is the main loop of the typical linenoise-based application.
     * The call to linenoise() will block as long as the user types something
     * and presses enter.
     *
     * The typed string is returned as a malloc() allocated string by
     * linenoise, so the user needs to free() it. */
    while((line = linenoise("hello> ")) != NULL) {
        /* Do something with the string. */
        if (line[0] != '\0' && line[0] != '/') {
            //printf("cmd: %s\n", line);
            ret = handle_command(line);
            if (ret == -1) {
                free(line);
                break;
            }
            linenoiseHistoryAdd(line); /* Add to the history. */
            linenoiseHistorySave(HISTORY_FILE); /* Save the history on disk. */
        } else if (!strncmp(line,"/historylen",11)) {
            /* The "/historylen" command will change the history len. */
            int len = atoi(line+11);
            linenoiseHistorySetMaxLen(len);
        } else if (line[0] == '/') {
            printf("Unreconized command: %s\n", line);
        }
        free(line);
    }
}

void MyNoise::add_completion(const QString& str, linenoiseCompletions *lc)
{
    QRegularExpression re("show\\s*(\\w+)");
    QRegularExpressionMatch rematch = re.match(str);
    bool hasMatch = rematch.hasMatch(); // true
    if (hasMatch) {
        add_complete_for_show(rematch.captured(1), lc);
        return;
    }

    if (str.trimmed().contains(QRegularExpression("show"))) {
        const QStringList& uilist = ActionHandler::getInstance()->getUiList();
        foreach (const QString& m, uilist) {
            QString cmd = QString("show %1").arg(m);
            linenoiseAddCompletion(lc, cmd.toUtf8());
        }
        return;
    }

    {
        // show command list
        QString re = QChar('^') + str.trimmed();
        const QStringList& matched =
            ActionHandler::getInstance()->getList().filter(QRegularExpression(re));
        foreach (const QString &m, matched) {
            linenoiseAddCompletion(lc, m.toUtf8());
        }
    }
}

void MyNoise::add_complete_for_show(const QString& str, linenoiseCompletions* lc)
{
#if 0
    (void)str;
    (void)lc;
#else
    //qDebug() << "add_complete_for_show:" << str;
    const QStringList& uilist = ActionHandler::getInstance()->getUiList();
    //qDebug() << "uilist:" << uilist;
    const QStringList& matched = uilist.filter(QRegularExpression(str));
    //qDebug() << "matched list:" << matched;
    foreach (const QString& m, matched) {
        QString cmd = QString("show %1").arg(m);
        linenoiseAddCompletion(lc, cmd.toUtf8());
    }

#endif
}

int MyNoise::handle_command(const QString& str)
{
    emit sigCommand(str);
    int ret = ActionHandler::getInstance()->getReturnCode();
    if (ret == ActionHandler::RET_EXIT) {
        return -1;
    }
    return 0;
}

char* MyNoise::add_hint(const QString& str)
{
    memset(myhint, 0, 80);
    if (str.trimmed() == "show") {
        //qDebug() << Q_FUNC_INFO << m_slist.at(0).toLatin1();
        //snprintf(myhint, 80, " %s", m_slist.at(0).toLatin1());
        snprintf(myhint, 80, "%s", "<uiname>");
        return myhint;
    }
    return NULL;
}
