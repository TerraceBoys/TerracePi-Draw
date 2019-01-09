#!/bin/sh

sudo apt-get update && sudo apt-get -y upgrade

sudo apt-get -y install python-dev python-imaging

cd ~/Desktop/TerracePi-Draw

if [ ! -f rgbmatrix.so ]; then
   wget https://github.com/adafruit/rpi-rgb-led-matrix/archive/master.zip
   unzip master.zip
   cd rpi-rgb-led-matrix-master
   make
   cp rgbmatrix.so cd ~/Desktop/TerracePi-Draw/
   cd cd ~/Desktop/TerracePi-Draw
   rm master.zip
   rm -rf rpi-rgb-led-matrix-master
fi

chmod +x ~/Desktop/TerracePi-Draw/refresh.sh
croncmd="~/Desktop/TerracePi-Draw/refresh.sh &"
cronjob="@reboot $croncmd"
( crontab -l | grep -v -F "$croncmd" ; echo "$cronjob" ) | crontab -

