# Copyright (C) 2015 Pegatron Corp.
SUMMARY = "Qt5 Car IVI demo"
DESCRIPTION = "Qt5 Car IVI demo application"
LICENSE = "Pegatron"
LIC_FILES_CHKSUM = "file://COPYING;md5=d41d8cd98f00b204e9800998ecf8427e"


S = "${TOPDIR}/../source/testtoolui"

EXTRA_OEMAKE = "'CXXFLAGS=-L${S}'"

require ${TOPDIR}/../meta-qt5/recipes-qt/qt5/qt5.inc
