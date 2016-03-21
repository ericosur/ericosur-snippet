SUMMARY = "Auto Time Zone"
LICENSE = "Pegatron"
COMPATIBLE_MACHINE = "(alt|gose|yose|lager)"
LIC_FILES_CHKSUM = "file://COPYING;md5=d41d8cd98f00b204e9800998ecf8427e"

#inherit autotools pkgconfig
#inherit autotools
#inherit pkgconfig
PACKAGES = "${PN} "

#S = "${TOPDIR}/../source/autotz"
S = "${WORKDIR}/autotz"

#TARGET_YOSEUI = "${TOPDIR}/../source/yoseui"

INHIBIT_PACKAGE_STRIP = "1"

addtask do_src before do_patch after do_unpack

do_src() {
    cp -rfp ${TOPDIR}/../source/autotz/ ${WORKDIR}/
}

#do_compile () {
#	oe_runmake
#}

do_install_append() {
#	rm -rf ${S}/patches

    #/usr/share/autotz_1.0/
    install -d ${D}${datadir}/yoseui-1.0

    #copy execution
    install -m 0755 ${B}/autotz ${D}${datadir}/yoseui-1.0
    #cp -rfp ${WORKDIR}/autotz/citieslist.txt /data/apps/yoseui/citieslist.txt
}

FILES_${PN} += " \
    ${datadir}/${P}/* \
    "
