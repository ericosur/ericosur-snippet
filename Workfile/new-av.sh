BOLD=`echo -e "\033[1;35m"`
OFFBOLD=`echo -e "\033[0m"`

# funciton to show help usage
show_help() {
cat << eot

${BOLD}NAME${OFFBOLD}
    avalon.sh - build avalon project

${BOLD}SYNOPSIS${OFFBOLD}
    avalon.sh -m <eng | user> [-f] [-3g] [-po] [-g] [-cb] [-cc]

${BOLD}OPTIONS${OFFBOLD}
    -m <mode>
        build the eng/user mode image
        DEFAULT is eng mode

    -f
        build factory mode image

    -3g
        build with 3G

    -po
        build with power off charge

    -cb
        build with clean build

    -cc
        setting up ccache

    -g
        turn off explicitly GMS integration into image
        DEFAULT the GMS will build into image

${BOLD}EXAMPLE${OFFBOLD}
    Build tostab12AL with different mode
         ./tostab12AL.sh -m eng
         ./tostab12AL.sh -m user
    
    build tostab12AL with factory image
         ./tostab12AL.sh -m eng -f

    build tostab12AL with clean build
         ./tostab12AL.sh -m eng -cb

    build tostab12AL with clean build and factory mode
         ./tostab12AL.sh -m eng -cb -f
eot
}

# this script should have at least one argument
if [ "$*" = "" ]; then
#	echo "no arg..."
	show_help
	exit 2
fi

args=`getopt df3:p:gc:m: $*`; err=$?
#echo args: $args
if [ $err -ne 0 ]; then
	echo "Parsing arugments error..."
	show_help
    exit 2
fi
set -- $args

# default values
# default GMS is on, use -g to toggle off
export BUILD_GMS_MODE=1
export BUILD_FACTORY_MODE=0
export SECURE_OS_BUILD=y
export BOARD_HAVE_3G=
export BUILD_SCRIPT_DEBUG=0
export POWEROFF_CHARGE=true
opt_cleanbuild=0
opt_ccache=0
topt="0"
popt="0"
bmode="eng"

# to toggle relative variables
for i
do
    case "$i"
    in
        -d)
            echo Script debugging mode!!!;
            export BUILD_SCRIPT_DEBUG=1;
            shift;;
        -g)
            #echo gms mode set; 
			export BUILD_GMS_MODE=0;
            shift;;
		-f)
            #echo factory mode; 
			export BUILD_FACTORY_MODE=1; 
            shift;;
        -c)
            #echo clean build option is "’"$2"’"; 
            if [ "$2" = "b" ]; then
                opt_cleanbuild=1
            fi
            if [ "$2" = "c" ]; then
                opt_ccache=1
            fi
            shift;
            shift;;
        -m)
            #echo mode is "’"$2"’"; 
			bmode="$2"; shift;
            shift;;
        -3)
            #echo 3 opt is "'"$2"'";
            #echo "board have 3g...";
            export BOARD_HAVE_3G=true;
            topt="$2"; shift;
            shift;;
        -p)
            #echo p opt is "'"$2"'";
            popt="$2"; shift;
            shift;;
        --)
            shift; break;;
    esac
done

#echo single-char flags: "’"$sflags"’"
#echo oarg is "’"$oarg"’"

echo "*** Buildng Project avalon !!! ***"
echo

echo "*** Building ["$bmode"] Mode Image!!! ***"

if [ $BUILD_FACTORY_MODE -eq 1 ]; then
	echo "*** Building Factory Mode Image!!! ***"
fi

if [ $BUILD_GMS_MODE -eq 1 ]; then
    echo "*** Building image with GMS integration ***"
fi

if [ "$BOARD_HAVE_3G" = "true" ]; then 
    echo "*** Build with 3G!!! *** "
#echo "BUILD_FACTORY_MODE"$BUILD_FACTORY_MODE
#echo "BUILD_GMS_MDOE"$BUILD_GMS_MODE
fi

export TOP=$PWD
export USE_CCACHE=1

if [ $opt_ccache -eq 1 ]; then
    echo "*** Setting up ccache to local ***"
    export CCACHE_DIR=$TOP/.ccache
    ccache -M 4G
# watch -n1 -d ccache -s
fi

export SECURE_OS_BUILD=y
export BOARD_VENDOR_HDCP_ENABLED=true
export ENABLE_SECURE_HDCP=1

if [ "$popt" = "o" ]; then
    echo "*** Build with Power Off Charge!!! ***"
    echo
    export POWEROFF_CHARGE=true
fi

if [ $BUILD_SCRIPT_DEBUG -ne 1 ]; then
    source build/envsetup.sh
    choosecombo 1 avalon $bmode
    #make clean-bootloader
fi

if [ $opt_cleanbuild -eq 1 ]; then
	 echo "*** Clean before building!!! ***"
    if [ $BUILD_SCRIPT_DEBUG -ne 1 ]; then
        make clean
        make nvidia-clean
    fi
fi

if [ $BUILD_SCRIPT_DEBUG -ne 1 ]; then
    time mp 2>&1 $* | tee buildlog.txt
fi

