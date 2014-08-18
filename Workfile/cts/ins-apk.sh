#!/bin/bash

# help to adb install 2 cts testing apk

CTSPATH=$HOME/cts/current-cts/repository/testcases

adb install $CTSPATH/CtsDelegatingAccessibilityService.apk

adb install $CTSPATH/CtsDeviceAdmin.apk

