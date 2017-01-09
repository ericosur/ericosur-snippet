#ifndef __TESTCASES_H__
#define __TESTCASES_H__

#include <QDebug>
#include <QString>
#include <QRegularExpression>
#include <QUrl>

void localre(const QString& re, const QString& str);
void testSizeOfDataType();
void testRegexp();
void testParseTPMS();
void testPercentEncoding();
QString translate_utf16be_to_qstring(const unsigned char utf16be[32]);
void testParseSysinfo();

void testblacklist();
bool isInBlackList(const QString& prop);
void testqurl();

#define PIDFILE    "/tmp/qretest.pid"


#endif  // __TESTCASES_H__
