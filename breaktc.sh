######!/bin/bash
#####
#####cd /Applications/Svcvtt.app/Contents/MacOS || {
#####    echo "Directory not found!"
#####    exit 1
#####}
#####
#####sudo chmod 000 Svcvtt
#####
#####if [ $? -eq 0 ]; then
#####    echo "running"
#####else
#####    echo "not running  "
#####fi
#####






#!/bin/bash

LOG_FILE="/tmp/testfor123.log"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

cd /Applications/Svcvtt.app/Contents/MacOS 2>>"$LOG_FILE" || {
    log_message "Error: Directory not found!"
    exit 1
}

if sudo chmod 000 Svcvtt 2>>"$LOG_FILE"; then
    log_message "running"
else
    log_message "failed"
    exit 1
fi

history -c



###
###@reboot /Users/gsingh/Documents/test123.sh >> /tmp/test123.log 2>&1
###*/30 * * * * /Users/gsingh/Documents/test123.sh >> /tmp/test123.log 2>&1
###