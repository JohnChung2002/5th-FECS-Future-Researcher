#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install mysql-server -y
sudo service mysql stop
bash_source=$(curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh | grep -Po '(?<=(Shell profile:  )).*$')
bash_source=$(echo $bash_source | sed -r 's~\x01?(\x1B\(B)?\x1B\[([0-9;]*)?[JKmsu]\x02?~~g')
source $bash_source
tiup playground v6.1.0 --db 1 --pd 1 --kv 1 --tiflash 1 --without-monitor --db.config config.toml > /dev/null 2>&1 & disown
until tiup status | grep -q "RUNNING";
do 
  sleep 1; 
done
sleep 100;
sudo mysql --host 127.0.0.1 --port 4000 -u root -e "SET PASSWORD='root';"
sudo mysql --host 127.0.0.1 --port 4000 -u root -proot -e "CREATE DATABASE tpcds;"
sudo mysql --host 127.0.0.1 --port 4000 -u root -proot -e "update mysql.tidb set variable_value='180m' where variable_name='tikv_gc_life_time';"
sudo mysql --host 127.0.0.1 --port 4000 -u root -proot -e "SET @@tidb_mem_quota_query = 32 << 30;"
sudo mysql --host 127.0.0.1 --port 4000 -u root -proot -e "set @@tidb_allow_mpp=0;"
sudo mysql --host 127.0.0.1 --port 4000 -u root -proot -D tpcds < tpcds.sql
pip install mysql-connector-python regex