#!/bin/bash

while true; do
    sudo socat pty,link="$BOT_BRIDGE_LOCATION" tcp:host.docker.internal:$BOT_BRIDGE_TCP_PORT > /dev/null 2>&1 &
    PID="$!"

    sleep 1
    
    if [[ -d /proc/$PID ]]; then
        wait $PID
    fi

    sleep 5
done