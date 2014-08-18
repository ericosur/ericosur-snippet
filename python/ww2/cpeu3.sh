#!/bin/bash

# path for my ipad1
EURO2=/var/mobile/Applications/7D9F41C7-E8ED-4E1B-9018-486A5887DE0D
EURO3=/var/mobile/Applications/3893A048-623C-47D7-9D96-934EC6FC4B9F
WW2=/var/mobile/Applications/3D5AA6A4-4091-4390-9B03-86213162C4C5

# scp game save from ipad
scp root@ipad:${EURO3}/Documents/commander.sav ./
scp root@ipad:${EURO3}/Documents/game0.sav ./
