#!/bin/bash

cd /home/ec2-user/build/
source ~/.bash_profile

# update ECS agent
sudo yum update -y ecs-init

# install docker
yum update -y
yum install -y docker

# start docker
service docker start

# give permissions to ec2-user
usermod -a -G docker ec2-user

# install docker compose
sudo curl -L `curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url | cut -d '"' -f 4 | sed -n '$p' | cut -f1-8 -d/`/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
sudo chmod +x /usr/local/bin/docker-compose


#install awslogs
sudo yum install -y awslogs
sudo service awslogs start


#set timezone to seoul

# sudo rm /etc/localtime
# sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime