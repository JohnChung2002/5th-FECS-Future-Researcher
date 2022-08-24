#!/bin/bash
cd /var/lib/mysql-files/
for s_f in `ls *dat`
do
    echo "[Processing] $s_f"
    sed 's/^|/0|/g;s/||/|0|/g;s/|$/|0/g' -i $s_f
done