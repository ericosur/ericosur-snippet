﻿@echo off
set _f=bar.dot

dot -Tgif -obar-dot.gif %_f%
fdp -Tgif -obar-fdp.gif %_f%
circo -Tgif -obar-circo.gif %_f%

set _f=
:end
 