sysbench oltp_common --threads=64 --rand-type=uniform --db-driver=pgsql --pgsql-db=sbtest --pgsql-host=127.0.0.1 --pgsql-port=5432 --pgsql-user=postgres --pgsql-password=postgres prepare --tables=16 --table-size=30000000
sysbench oltp_read_write --threads=64 --time=1200 --report-interval=1 --rand-type=uniform --db-driver=pgsql --pgsql-db=sbtest --pgsql-host=127.0.0.1 --pgsql-port=5432 --pgsql-user=postgres --pgsql-password=postgres run --tables=16 --table-size=30000000 > psql_30mil_read_write.txt
sysbench oltp_point_select --threads=64 --time=1200 --report-interval=1 --rand-type=uniform --db-driver=pgsql --pgsql-db=sbtest --pgsql-host=127.0.0.1 --pgsql-port=5432 --pgsql-user=postgres --pgsql-password=postgres run --tables=16 --table-size=30000000 > psql_30mil_point_select.txt
sysbench oltp_update_non_index --threads=64 --time=1200 --report-interval=1 --rand-type=uniform --db-driver=pgsql --pgsql-db=sbtest --pgsql-host=127.0.0.1 --pgsql-port=5432 --pgsql-user=postgres --pgsql-password=postgres run --tables=16 --table-size=30000000 > psql_30mil_update_non_index.txt
sysbench oltp_update_index --threads=64 --time=1200 --report-interval=1 --rand-type=uniform --db-driver=pgsql --pgsql-db=sbtest --pgsql-host=127.0.0.1 --pgsql-port=5432 --pgsql-user=postgres --pgsql-password=postgres run --tables=16 --table-size=30000000 > psql_30mil_update_index.txt