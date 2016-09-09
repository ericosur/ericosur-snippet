/** \file mynoise.h
**/
#ifndef __MY_NOISE_H__
#define __MY_NOISE_H__

#include <QObject>
#include <QString>
#include <QStringList>

#include "actionhandler.h"
extern "C" {
#include "linenoise.h"
}

class MyNoise : public QObject
{
    Q_OBJECT
public:
    static MyNoise* getInstance();

    void setup();
    void startcommandloop();
    void add_completion(const QString& str, linenoiseCompletions* lc);
    int handle_command(const QString& str);
    char* add_hint(const QString& str);

protected:
    static MyNoise* _instance;
    explicit MyNoise();

    void add_complete_for_show(const QString& str, linenoiseCompletions* lc);

signals:
    void sigCommand(const QString& cmd);

private:

};

#endif  // __MY_NOISE_H__
