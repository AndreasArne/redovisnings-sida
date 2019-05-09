apt-get install -y ufw
ufw allow ssh
ufw allow http
ufw allow 443/tcp
ufw --force enable
ufw status