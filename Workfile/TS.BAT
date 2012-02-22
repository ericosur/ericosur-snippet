rem make datetime stamp by using 'for'

for /f "tokens=1,2,3,4 delims=/ " %%a in ("%DATE%") do set DATESTAMP=%%a%%b%%c

echo %DATESTAMP%
