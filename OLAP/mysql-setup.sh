sudo apt update
sudo apt upgrade -y
sudo apt install mysql-server -y
sudo service mysql restart
sudo service mysql start
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';"
sudo mysql -u root -proot -e "CREATE DATABASE tpcds;"
sudo mysql -u root -proot -D tpcds < tpcds.sql
pip install mysql-connector-python regex
./prepare-data-gen.sh