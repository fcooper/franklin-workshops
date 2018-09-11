#!/bin/bash

sudo cp bb-wl18xx /etc/default/bb-wl18xx
sudo cp /etc/default/bb-wl18xx /etc/default/bb-wl18xx_bak
eval "sed -i -e 's/USE_PERSONAL_SSID=\"BeagleBone\"/USE_PERSONAL_SSID=\"$1\"/g' /etc/default/bb-wl18xx"

eval "sed -i -e 's/USE_PERSONAL_PASSWORD=\"BeagleBone\"/USE_PERSONAL_PASSWORD=\"beaglebone_$2\"/g' /etc/default/bb-wl18xx"

sed -i -e 's/USE_APPENDED_SSID=yes/USE_APPENDED_SSID=no/g' /etc/default/bb-wl18xx

