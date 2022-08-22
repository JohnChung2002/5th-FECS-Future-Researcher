sudo apt update
sudo apt upgrade -y
curl https://install.citusdata.com/community/deb.sh | sudo bash
sudo apt-get -y install postgresql-14-citus-11.0 sysbench
cp postgresql.conf.sample /usr/share/postgresql/14/postgresql.conf.sample
sudo -u postgres export PATH=$PATH:/usr/lib/postgresql/14/bin
sudo -u postgres mkdir ~/citus
sudo -u postgres initdb -D citus
sudo -u postgres echo "shared_preload_libraries = 'citus'" >> citus/postgresql.conf
sudo -u postgres pg_ctl -D citus -o "-p 9700" -l citus_logfile start
sudo -u postgres psql -p 9700 -c "CREATE EXTENSION citus;"
sudo -u postgres psql -p 9700 -c "select citus_version();"
sudo -u postgres psql -p 9700 -c "ALTER USER postgres with password 'postgres';"
sudo -u postgres psql -p 9700 -c "CREATE DATABASE sbtest;"