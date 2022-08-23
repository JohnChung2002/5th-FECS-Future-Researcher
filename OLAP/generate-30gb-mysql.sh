cd tpcds-kit/tools
./dsdgen -scale 30 -f -dir /var/lib/mysql-files/ –parallel 8 –child 1 &
./dsdgen -scale 30 -f -dir /var/lib/mysql-files/ –parallel 8 –child 2 &
./dsdgen -scale 30 -f -dir /var/lib/mysql-files/ –parallel 8 –child 3 &
./dsdgen -scale 30 -f -dir /var/lib/mysql-files/ –parallel 8 –child 4 &
./dsdgen -scale 30 -f -dir /var/lib/mysql-files/ –parallel 8 –child 5 &
./dsdgen -scale 30 -f -dir /var/lib/mysql-files/ –parallel 8 –child 6 &
./dsdgen -scale 30 -f -dir /var/lib/mysql-files/ –parallel 8 –child 7 &
./dsdgen -scale 30 -f -dir /var/lib/mysql-files/ –parallel 8 –child 8 &