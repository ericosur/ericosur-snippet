SUMMARY = "message queue tester"
LICENSE = "GPLv2"
COMPATIBLE_MACHINE = "(alt|gose|yose|lager)"
LIC_FILES_CHKSUM = "file://COPYING;md5=d41d8cd98f00b204e9800998ecf8427e"

#inherit autotools pkgconfig
#inherit autotools
#inherit pkgconfig
PACKAGES = "${PN} "

S = "${WORKDIR}/adasmsgq"

addtask do_src before do_patch after do_unpack

do_src() {
    cp -rfp ${TOPDIR}/../source/adasmsgq/  ${WORKDIR}/
}

do_compile () {
    oe_runmake
}

#FILES_${PN}-staticdev = "${libdir}/*.a"
