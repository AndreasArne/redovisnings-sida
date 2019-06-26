cp infrastructure-as-code/scripts/resources/nginx.conf /etc/nginx/sites-available/<filename>

cd /etc/nginx/sites-enabled && sudo ln -s /etc/nginx/sites-available/<filename>

sudo nginx -t && sudo service nginx restart



# https
sed -i 's/# deb http://mirrors.digitalocean.com/debian stretch-backports main contrib non-free/deb http://mirrors.digitalocean.com/debian stretch-backports main contrib non-free/' /etc/apt/sources.list
sed -i 's/# http://mirrors.digitalocean.com/debian stretch-backports main contrib non-free/http://mirrors.digitalocean.com/debian stretch-backports main contrib non-free/' /etc/apt/sources.list

sudo apt-get update
sudo apt-get install python-certbot-nginx -t stretch-backports

sudo certbot --nginx # need manuell input

cat infrastructure-as-code/scripts/resources/nginx_https.conf > /etc/nginx/sites-available/<filename>

sudo nginx -t && sudo service nginx restart