#!/bin/bash
# Replace NULL with 0 in the first field to convert ^| into 0|.
# Replace NULL with 0 in the fields in the middle to convert || into |0|.
# Replace NULL with 0 in the last field to convert |$ into |0.
cd /var/lib/mysql-files/
for s_f in `ls *dat`
do
    echo "[Processing] $s_f"
    while [ `egrep '\|\||^\||\|$' $s_f |wc -l` -gt 0 ]
    do 
        sed 's/^|/0|/g;s/||/|0|/g;s/|$//g' -i $s_f
    done
done
for s_f in item.dat store.dat web_page.dat web_site.dat call_center.dat
do
# Process the first and second date-typed fields whose value is NULL.
sed 's/^\([A-Za-z0-9]*|[A-Za-z0-9]*\)|0|0|\(.*\)/\1|0000-00-00|0000-00-00|\2/' -i $s_f
# Process the second date-typed field whose value is NULL.
sed 's/^\([0-9A-Za-z]*|[A-Za-z0-9]*|[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}\)|0|\(.*\)/\1|0000-00-00|\2/' -i $s_f
# Process the first date-typed field whose value is NULL.
sed 's/^\([0-9A-Za-z]*|[A-Za-z0-9]*\)|0|\([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}|.*\)/\1|0000-00-00|\2/' -i $s_f
done