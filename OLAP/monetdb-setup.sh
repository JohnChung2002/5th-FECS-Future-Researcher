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
sudo apt-get install gcc make flex bison byacc git -y
git clone https://github.com/gregrahn/tpcds-kit.git
cd tpcds-kit/tools
make OS=LINUX
./dsdgen -scale 30 -f -dir /tmp
pip install pymonetdb