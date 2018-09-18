sudo rm -rf /var/www/html/workshop > /dev/null
sudo mkdir /var/www/html/workshop/
sudo mkdir /var/www/html/workshop/bopit
sudo cp -r ../workshop/bopit/webpage/* /var/www/html/workshop/bopit

sudo cp ../workshop/workshop.py /usr/local/lib/python2.7/dist-packages/workshop.py

sudo apt-get install -y python-flask
yes | sudo pip install flask-cors
