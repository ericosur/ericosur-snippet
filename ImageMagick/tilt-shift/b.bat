rem revised on Jul 24 2012

convert in.jpg -sigmoidal-contrast 15x30%% ( +clone -sparse-color Barycentric "0,0 black 0,%%[fx:h-1] gray80" -solarize 50%% -level 50%%,0 ) -compose Blur -set "option:compose:args 15" -composite final.jpg
