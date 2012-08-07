@echo off

rem revised on Jul 24 2012

set IN=in.jpg
set TIM=tmp.jpg
set OUT=out.jpg

convert %IN% -sigmoidal-contrast 15x40%% %TIM%
convert %TIM% -sparse-color Barycentric "0,0 black 0,%%h white" -function polynomial "4,-4,1" blur.jpg
convert %TIM% blur.jpg -compose Blur -set "option:compose:args 10" -composite %OUT%

