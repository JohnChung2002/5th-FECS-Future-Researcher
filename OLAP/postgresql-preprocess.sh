#!/bin/bash
# Replace NULL with 0 in the first field to convert ^| into 0|.
# Replace NULL with 0 in the fields in the middle to convert || into |0|.
# Replace NULL with 0 in the last field to convert |$ into |0.
cd /tmp
for s_f in `ls *dat`
do
    echo "[Processing] $s_f"
    sed -i 's/|$//' $s_f
done