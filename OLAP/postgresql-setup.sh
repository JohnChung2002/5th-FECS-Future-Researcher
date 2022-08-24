sudo apt update
sudo apt upgrade -y
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt update
sudo apt -y install postgresql-14 libpq-dev
cp postgresql.conf.sample /usr/share/postgresql/14/postgresql.conf.sample
pg_createcluster 14 main --start
sudo -u postgres psql -c "ALTER USER postgres with password 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE tpcds;"
sudo service postgresql restart
sudo -u postgres psql -d tpcds < tpcds.sql
pip install psycopg2 regex
./prepare-data-gen.sh