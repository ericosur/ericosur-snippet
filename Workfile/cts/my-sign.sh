#!/bin/bash

# use signapk.jar to sign platform key to specific apk

SIGNAPK=out/host/linux-x86/framework/signapk.jar
X509=vendor/pega/security/duke/platform.x509.pem
PK8=vendor/pega/security/duke/platform.pk8
INAPK=DukeWiFiPortableOff.apk
OUTAPK=DukeWiFiPortableOff-sign.apk

java -jar $SIGNAPK $X509 $PK8 $INAPK $OUTAPK



