#!/bin/bash

#pwd
START=android-4.0.4_r2.1
STOP=android-4.1.1_r1

git log --format='%h %ai, %an, %s' ${START}..${STOP}

