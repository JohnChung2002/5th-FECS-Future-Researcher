#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install mysql-server sysbench -y
sudo service mysql stop
bash_source=$(curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh | grep -Po '(?<=(Shell profile:  )).*$')
bash_source=$(echo $bash_source | sed -r 's~\x01?(\x1B\(B)?\x1B\[([0-9;]*)?[JKmsu]\x02?~~g')
source $bash_source
tiup playground v6.1.0 --db 1 --pd 1 --kv 1 --tiflash 1 --without-monitor > /dev/null 2>&1 & disown
until tiup status | grep -q "RUNNING";
do 
  sleep 1; 
done
sudo mysql --host 127.0.0.1 --port 4000 -u root -e "SET PASSWORD='root';"
sudo mysql --host 127.0.0.1 --port 4000 -u root -proot -e "CREATE DATABASE sbtest;"