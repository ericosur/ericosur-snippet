#!/bin/sh

# use bash shell script to count numbers
#
# 2006/12/27 by ericosur
#

LIMIT=50

for ((i=0; i <= LIMIT; i++))
do
	if [ $i -lt 10 ] ; then
		echo -n "00$i "
	else
		echo -n "0$i "
	fi
done

echo ; echo
#echo $STR

i=0
variable2=`while [ "$i" -le 50 ]
do
	if [ $i -lt 10 ] ; then
		echo -n "lk00$i "
	else
		echo -n "lk0$i "
	fi

	let "i += 1"                 # Increment.
done`

echo "variable2 = $variable2"

mycmd=`echo -n "cat $variable2 > x.tgz"`
echo $mycmd
`$mycmd`

