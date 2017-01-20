# Copyright (C) 2015 Pegatron Corp.
SUMMARY = "Qt5 Car IVI demo"
DESCRIPTION = "Qt5 Car IVI demo application"
LICENSE = "Pegatron"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/Pegatron;md5=8dbf761840bdb42cf94b2d15b5dfaa82"

S = "${WORKDIR}/polldev"
CXXFLAGS += "-I${STAGING_INCDIR}/libhu-1.0 "
CXXFLAGS += "-I${STAGING_INCDIR}/libmsgq-1.0 "

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
