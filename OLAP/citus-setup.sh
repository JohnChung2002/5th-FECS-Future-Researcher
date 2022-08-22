sudo apt update
sudo apt upgrade -y
curl https://install.citusdata.com/community/deb.sh | sudo bash
sudo apt-get -y install postgresql-14-citus-11.0 sysbench
cp postgresql.conf.sample /usr/share/postgresql/14/postgresql.conf.sample
sudo su - postgres
export PATH=$PATH:/usr/lib/postgresql/14/bin
cd ~
mkdir citus
initdb -D citus
echo "shared_preload_libraries = 'citus'" >> citus/postgresql.conf
pg_ctl -D citus -o "-p 9700" -l citus_logfile start
psql -p 9700 -c "CREATE EXTENSION citus;"
psql -p 9700 -c "select citus_version();"
psql -p 9700 -c "ALTER USER postgres with password 'postgres';"
exit
sudo -u postgres psql -p 9700 -c "CREATE DATABASE tpcds;"