# Copyright (C) 2015 Pegatron Corp.
SUMMARY = "Qt5 Car IVI Test Tool"
DESCRIPTION = "Qt5 Car IVI test tool application"
LICENSE = "Pegatron"
LIC_FILES_CHKSUM = "file://COPYING;md5=d41d8cd98f00b204e9800998ecf8427e"


#S = "${TOPDIR}/../source/testtoolui"
S = "${WORKDIR}/testtoolui"

EXTRA_OEMAKE = "'CXXFLAGS=-L${S}'"

require ${TOPDIR}/../meta-qt5/recipes-qt/qt5/qt5.inc

do_src() {
    cp -rfp ${TOPDIR}/../source/testtoolui ${WORKDIR}
}

addtask do_src before do_patch after do_unpack

do_install() {
    install -d ${D}${datadir}/${P}
    install -m 0755 ${B}/testtool ${D}${datadir}/${P}
	install -m 0755 ${S}/testtool.conf ${D}${datadir}/${P}
}

FILES_${PN}-dbg += "${datadir}/${P}/.debug"
FILES_${PN} += "${datadir}"
