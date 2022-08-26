sudo apt update
sudo apt upgrade -y
echo 'deb https://dev.monetdb.org/downloads/deb/ focal monetdb\ndeb-src https://dev.monetdb.org/downloads/deb/ focal monetdb' > /etc/apt/sources.list.d/monetdb.list
sudo wget --output-document=/etc/apt/trusted.gpg.d/monetdb.gpg https://dev.monetdb.org/downloads/MonetDB-GPG-KEY.gpg
sudo apt-key finger
sudo apt update
sudo apt install monetdb5-sql monetdb-client -y
monetdbd create ~/tpcds
monetdbd start ~/tpcds
monetdb create tpcds
monetdb start tpcds
echo "user=monetdb\npassword=monetdb" > /var/lib/monetdb/.monetdb
export DOTMONETDBFILE="/var/lib/monetdb/.monetdb"
mclient -d tpcds < tpcds.sql
pip install pymonetdb regex