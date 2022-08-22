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