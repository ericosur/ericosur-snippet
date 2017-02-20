# Copyright (C) 2015 Pegatron Corp.
SUMMARY = "Qt5 Dialog Control"
DESCRIPTION = "Qt5 dialog control application"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

require ${TOPDIR}/../meta-qt5/recipes-qt/qt5/qt5.inc

MYSRC = "/src/snippet/qt/srcsink/mylib"
S = "${WORKDIR}/mylib/"

CXXFLAGS += "-DUSE_YOSETARGET"

DEPENDS = "libxml2 qtdeclarative qtgraphicaleffects"
RDEPENDS_${PN} = "qtdeclarative-qmlplugins qtgraphicaleffects-qmlplugins"

addtask do_src before do_patch after do_unpack

do_src() {
    cp -rfp ${MYSRC} ${WORKDIR}/
}

do_install() {
	install -d ${D}${libdir}
	install -m 0755 ${B}/libmylib.a ${D}${libdir}
}

#INHIBIT_PACKAGE_DEBUG_SPLIT = "1"
#INHIBIT_PACKAGE_STRIP = "1"
