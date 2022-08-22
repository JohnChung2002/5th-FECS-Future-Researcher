sudo apt update
sudo apt upgrade -y
sudo apt install mysql-server sysbench -y
sudo service mysql stop
curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh
tiup playground v6.1.0 --db 1 --pd 1 --kv 1 --tiflash 1 --without-monitor &
sudo mysql --host 127.0.0.1 --port 4000 -u root -p -e "SET PASSWORD='root';"
sudo mysql --host 127.0.0.1 --port 4000 -u root -proot -e "CREATE DATABASE sbtest;"