sudo apt update
sudo apt upgrade -y
curl https://install.citusdata.com/community/deb.sh | sudo bash
sudo apt-get -y install postgresql-14-citus-11.0 libpq-dev
cp postgresql.conf.sample /usr/share/postgresql/14/postgresql.conf.sample
sudo cp citus-addon.sh /var/lib/postgresql
sudo su -c "./citus-addon.sh" postgres
sudo -u postgres psql -p 9700 -c "CREATE DATABASE tpcds;"
pip install psycopg2 regex
python citus-table.py