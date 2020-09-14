#!/bin/bash
ip="52.169.116.101"

rsync -avzr -e "ssh -i ~/.ssh/id_rsa" 10-first-minutes azureuser@$ip:
ssh azureuser@$ip
sudo su
cd 10-first-minutes/
sh 1.update.sh
sh 2.new_user.sh
sh 3.firewall.sh
sh 4.install.sh
exit

ssh deploy@$ip
sudo userdel -r azureuser
exit

rsync -avrz ../../redovisnings-sida deploy@52.169.116.101:
ssh deploy@$ip
# git clone https://github.com/AndreasArne/redovisnings-sida.git
mv redovisnings-sida microblog
cd microblog
rm -rf venv
sh scripts/deploy-app/1.dependencies.sh
sh scripts/deploy-app/2.microblog.sh
sh scripts/deploy-app/3.db.sh
sh scripts/deploy-app/4.supervisor.sh
sudo sh scripts/deploy-app/5.nginx.sh

sudo sh scripts/docker/1.install.sh
sudo sh scripts/docker/2.compose.sh
