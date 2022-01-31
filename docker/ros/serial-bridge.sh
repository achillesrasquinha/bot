#!/bin/bash

while true; do
    sudo socat pty,link="$BOT_BRIDGE_LOCATION" tcp:$BOT_BRIDGE_TCP_HOST:$BOT_BRIDGE_TCP_PORT # > /dev/null 2>&1 &

    PID="$!"

    sleep 1
    
    if [[ -d /proc/$PID ]]; then
        echo "Connected to bridge $BOT_BRIDGE_LOCATION via $BOT_BRIDGE_TCP_HOST:$BOT_BRIDGE_TCP_PORT.";
        wait $PID;
    fi

    sleep 5
done