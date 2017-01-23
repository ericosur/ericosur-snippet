# Copyright (C) 2015 Pegatron Corp.
SUMMARY = "Qt5 Car IVI demo"
DESCRIPTION = "Qt5 Car IVI demo application"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

S = "${WORKDIR}/polldev"
CXXFLAGS += "-DUSE_YOSETARGET "
CXXFLAGS += "-I${STAGING_INCDIR}/libhu-1.0 "
CXXFLAGS += "-I${STAGING_INCDIR}/libmsgq-1.0 "
CXXFLAGS += "-lhu -lmsgq"

DEPENDS = "qtbase qtconnectivity libhu libmsgq"
RDEPENDS_${PN} = "qtbase qtconnectivity libhu libmsgq"

require ${TOPDIR}/../meta-qt5/recipes-qt/qt5/qt5.inc

addtask do_src before do_patch after do_unpack

do_src() {
    cp -rfp /src/snippet/qt/polldev ${WORKDIR}/
}

do_install() {
    install -d ${D}${sbindir}
    install -m 0755 ${B}/polldev ${D}${sbindir}/polldev
}
