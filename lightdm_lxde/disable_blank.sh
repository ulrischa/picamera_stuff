#!/bin/bash
if [ -z "$DISPLAY" ]
then
    export DISPLAY=:0
fi
# Portrait mode
#xrandr --output `xrandr -q | grep " connected" | awk '{print $1}'` --rotate left
#xrandr --output `xrandr -q | grep " connected" | awk '{print $1}'` --rotate right
# Disable blanking
setterm -blank 0 -powerdown 0
xset s noblank
xset s off
xset -dpms
