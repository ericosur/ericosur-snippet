/**
 * \file pass.h
 */

#ifndef __PASS_H__
#define __PASS_H__

#include <QObject>
#include <QString>
#include <QCryptographicHash>

#define CIPHER_HASH   "81dc9bdb52d04dc20036dbd8313ed055"

QString md5sum(const char* buffer, int size);

// may validate by using
// echo -n "1234" |openssl dgst -sha1 -hmac "key"|sed -e "s/^.*\ //"
// vs
// hmacSha1("1234", "key")
QString hmacSha1(QByteArray key, QByteArray baseString);

#endif  // __PASS_H__
