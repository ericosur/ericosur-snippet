#!/bin/bash
#
# use svn to fetch sub-folder from my own github snippet
# use browser to see git log from:
# https://github.com/ericosur/ericosur-snippet/tree/master/qt/dirtest
#

GITHUB=https://github.com/ericosur/myqt

svn export $GITHUB/trunk/dirtest/
svn export $GITHUB/trunk/srcsink/

