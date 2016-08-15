# Copyright (C) 2015 Pegatron Corp.
SUMMARY = "Qt5 Dialog Control"
DESCRIPTION = "Qt5 dialog control application"
LICENSE = "Pegatron"
LIC_FILES_CHKSUM = "file://COPYING;md5=d41d8cd98f00b204e9800998ecf8427e"

require ${TOPDIR}/../meta-qt5/recipes-qt/qt5/qt5.inc

S = "${WORKDIR}/qtchat/"

DEPENDS = "libxml2 qtdeclarative qtgraphicaleffects"
RDEPENDS_${PN} = "qtdeclarative-qmlplugins qtgraphicaleffects-qmlplugins"

addtask do_src before do_patch after do_unpack

do_src() {
    cp -rfp ${TOPDIR}/../source/qtchat/  ${WORKDIR}/
}

do_install() {
	install -d ${D}${sbindir}
	install -m 0755 chat ${D}${sbindir}/qtchat
}

#INHIBIT_PACKAGE_DEBUG_SPLIT = "1"
#INHIBIT_PACKAGE_STRIP = "1"
