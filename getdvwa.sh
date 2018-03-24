
#!/bin/bash

#from this: https://th3phantoms.blogspot.com/2017/04/install-dvwa-on-ubuntu-server-1604.html

#get root
sudo -s

#get packages
apt-get install apache2 -y      #apache2
apt-get install git     -y      #git
apt-get install libapache2-mod-php7.0 libapache2-mod-fastcgi php7.0-fpm php7.0 php-mysql php7.0-mbstrin$

#get dvwa
cd /var/www
git clone https://github.com/ethicalhack3r/DVWA.git
mv DVWA-master dvwa

#start apache2
service apache2 start

#set permissions
chmod 777 /var/www/html/dvwa/hackable/uploads/
chmod 777 /var/www/html/dvwa/hackable/uploads/

#Next steps
echo "Next Steps:\n"
echo "1. In /var/www/html/dvwa/config/config.inc.php:\n"
echo "   find $_DVWA[ 'db_password' ] = 'p@ssw0rd';\n"
echo "   and change the mysql password."
echo "\n"
echo "2. Create the DVWA database:\n"
echo "   mysql -y root -p\n"
echo "   create database dvwa;\n"
echo "   exit\n"
echo "3. Reset database and restart apache2:\n"
echo "   http://<ip>/dvwa/\n"
echo "   scroll down and find the create/reset database button\n"
echo "   service apache2 restart"

