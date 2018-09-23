echo "tempwd" | sudo -S apt-get update
echo "tempwd" | sudo apt-get install -y python-flask python-smbus python3-smbus python-pip
yes | sudo pip install flask-cors

file="/boot/uEnv.txt_bak"
if [ -f "$file" ]
then
	echo "$file found."
else
	echo "$file not found."
	echo "tempwd" | sudo cp /boot/uEnv.txt /boot/uEnv.txt_bak
fi

echo "tempwd" | sudo sed -i.bak s/#disable_uboot_overlay_video=1/disable_uboot_overlay_video=1/ /boot/uEnv.txt


echo "tempwd" | sudo rm -rf /lib/systemd/system/bonescript*


file="/etc/apache2/mods-available/mpm_event.conf_bak"
if [ -f "$file" ]
then
	echo "$file found."
else
	echo "$file not found."
	echo "tempwd" | sudo cp   /etc/apache2/mods-available/mpm_event.conf /etc/apache2/mods-available/mpm_event.conf_bak
	echo "tempwd" | sudo cp   /etc/apache2/mods-available/mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf_bak
	echo "tempwd" | sudo cp   /etc/apache2/mods-available/mpm_worker.conf /etc/apache2/mods-available/mpm_worker.conf_bak
fi


echo "tempwd" | sudo cp mpm* /etc/apache2/mods-available/


echo "tempwd" | sudo rm -rf /var/www/html/workshop > /dev/null
echo "tempwd" | sudo mkdir /var/www/html/workshop/
echo "tempwd" | sudo mkdir /var/www/html/workshop/bopit
echo "tempwd" | sudo cp -r ../workshop/bopit/webpage/* /var/www/html/workshop/bopit
echo "tempwd" | sudo cp ../workshop/workshop.py /usr/local/lib/python2.7/dist-packages/workshop.py




echo "tempwd" | sudo cp bb-wl18xx /etc/default/bb-wl18xx

file="/etc/default/bb-wl18xx_bak"
if [ -f "$file" ]
then
	echo "$file found."
else
	echo "$file not found."
	echo "tempwd" | sudo cp /etc/default/bb-wl18xx /etc/default/bb-wl18xx_bak
fi

echo "tempwd" | sudo eval "sed -i -e 's/USE_PERSONAL_SSID=\"BeagleBone\"/USE_PERSONAL_SSID=\"$1\"/g' /etc/default/bb-wl18xx"

echo "tempwd" | sudo eval "sed -i -e 's/USE_PERSONAL_PASSWORD=\"BeagleBone\"/USE_PERSONAL_PASSWORD=\"beaglebone_$2\"/g' /etc/default/bb-wl18xx"

echo "tempwd" | sudo sed -i -e 's/USE_APPENDED_SSID=yes/USE_APPENDED_SSID=no/g' /etc/default/bb-wl18xx

