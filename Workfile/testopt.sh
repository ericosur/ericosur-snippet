BOLD=`echo -e "\033[1;35m"`
OFFBOLD=`echo -e "\033[0m"`

# funciton to show help usage
show_help() {
cat << eot

${BOLD}NAME${OFFBOLD}
    testopt.sh - build script

${BOLD}SYNOPSIS${OFFBOLD}
    testopt.sh -m <eng | user>

${BOLD}OPTIONS${OFFBOLD}
    -m <mode>
        build the eng/user mode image

    -cb
        build with clean build

    -f
        build factory mode image

    -g
        turn on GMS integration into image

${BOLD}EXAMPLE${OFFBOLD}
    Build with different mode
         ./testopt.sh -m eng
         ./testopt.sh -m user

    build with factory image
         ./testopt.sh -m eng -f

    build with clean build
         ./testopt.sh -m eng -cb

    build with clean build and factory mode
         ./testopt.sh -m eng -cb -f

eot
}

# this script should have at least one argument
if [ "$*" = "" ]; then
#	echo "no arg..."
	show_help
	exit 2
fi

args=`getopt gfc:m: $*`; err=$?
#echo args: $args
if [ $err -ne 0 ]; then
	echo "Parsing arugments error..."
	show_help
    exit 2
fi
set -- $args

# default values
export BUILD_GMS_MODE=0
export BUILD_FACTORY_MODE=0
copt="0"
bmode="eng"

# to toggle relative variables
for i
do
    case "$i"
    in
        -g)
            #echo gms mode set;
			export BUILD_GMS_MODE=1;
            shift;;
		-f)
            #echo factory mode;
			export BUILD_FACTORY_MODE=1;
            shift;;
        -c)
            #echo clean build option is "’"$2"’";
			copt="$2"; shift;
            shift;;
        -m)
            #echo mode is "’"$2"’";
			bmode="$2"; shift;
            shift;;
        --)
            shift; break;;
    esac
done

#echo single-char flags: "’"$sflags"’"
#echo oarg is "’"$oarg"’"

echo "*** Buildng Project test!!! ***"
echo

echo "*** Building ["$bmode"] Mode Image!!! ***"

if [ $BUILD_FACTORY_MODE -eq 1 ]; then
	echo "*** Building Factory Mode Image!!! ***"
fi

if [ $BUILD_GMS_MODE -eq 1 ]; then
    echo "*** Building image with GMS integration ***"
fi

#echo "BUILD_FACTORY_MODE"$BUILD_FACTORY_MODE
#echo "BUILD_GMS_MDOE"$BUILD_GMS_MODE

export TOP=$PWD
export USE_CCACHE=1

source build/envsetup.sh
choosecombo 1 test $bmode
make clean-bootloader

if [ "$copt" = "b" ]; then
	echo "*** Clean before building!!! ***"
	make clean
fi

mp 2>&1 | tee buildlog.txt

