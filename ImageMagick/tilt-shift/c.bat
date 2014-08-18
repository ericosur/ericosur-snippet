set img=IMG_3391.jpg

convert %img% -sigmoidal-contrast 10x40%% ( +clone -sparse-color Barycentric "0,0 black 0,%%[fx:h-1] white" -solarize 50%% -level 50%%,0 ) -compose Blur -set option:compose:args 15 -composite tilt-shift.jpg

@rem 0,%%[fx:h-1] white
