apt-get -y remove --purge unscd
userdel -r debian
useradd deploy
mkdir /home/deploy
mkdir /home/deploy/.ssh
chmod 700 /home/deploy/.ssh

usermod -s /bin/bash deploy

#echo -e "<password>\n<password>" | passwd deploy # echo "<password>" | passwd --stdin deploy om nyare version
echo "deploy:<passwd>" | chpasswd
usermod -aG sudo deploy # lägg till i sudo grupp

# har redan lagt  ssh nyckel, när droplet skapades. Kopiera från root
cp ~/.ssh/authorized_keys /home/deploy/.ssh/
chown deploy:deploy /home/deploy -R # Sätt deploy som ägare för dir och filer

sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
echo "\nAllowUsers deploy" >> /etc/ssh/sshd_config
service ssh restart

echo "deploy ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
