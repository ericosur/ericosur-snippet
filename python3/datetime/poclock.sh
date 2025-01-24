#!/bin/bash
#
# refer to: https://mikebuss.com/2014/01/03/push-notifications-cli/
#
# 2024/3/7  tell the clock
#

VERSION=2025.01.22

function die() {
  local message="$1"
  echo "ERROR: $message" >&2
  exit 1
}

function in_vacation() {
    local start_date="2025-01-25 00:00:00"
    local end_date="2025-02-02 23:59:59"

    local start_timestamp=$(date -d "$start_date" +%s)
    local end_timestamp=$(date -d "$end_date" +%s)
    local current_timestamp=$(date +%s)

    if [[ $current_timestamp -ge $start_timestamp &&  $current_timestamp -le $end_timestamp ]] ; then
        echo "in vocation..."
        exit 1
    fi
}

# if datetime in vacation, exit...
in_vacation

#conf=$HOME/bin/pushover-net.json
#APP_TOKEN=$(jq .apitoken ${conf} | sed 's/\"//g')
#USER_KEY=$(jq .userkey ${conf} | sed 's/\"//g')
#
# NOTE: hard code app token and user key here
#
APP_TOKEN=xxxxxx
USER_KEY=xxxxxx

if [ "${APP_TOKEN}" == "" ] && [ "${USER_KEY}" == "" ] ; then
    die "no APP_TOKEN and USER_KEY"
fi


RET=$1
MESSAGE=$2
TITLE=$(hostname)

# compose the message
TS=$(date +%H:%M)
clock_emoji=$(clockemoji.py)
MESSAGE="It is ${TS}. ${clock_emoji}"

# debug
#echo "MESSAGE: $MESSAGE"

function send_notification() {
    local PREFERDEV="$1"

    #dt=$(date "+%D %T")
    #msg="$* ${dt}"
    printf "title: %s\nmessage: %s\ndevice: %s\n" "${TITLE}" \
        "${MESSAGE}" "${PREFERDEV}"

    curl -s \
        -F "token=${APP_TOKEN}" \
        -F "user=${USER_KEY}" \
        -F "title=From ${HOSTNAME}" \
        -F "device=${PREFERDEV}"    \
        -F "message=${MESSAGE}" \
        https://api.pushover.net/1/messages.json

    STAMP=$(TZ=Asia/Taipei date --iso-8601=min)

    echo -e "\n$STAMP"
    echo "curl exit code: $?"
}

# here call function to send to different devices
send_notification "i16pm"
sleep 2
send_notification "pixel6a"
