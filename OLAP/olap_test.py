import mysql.connector
import time
import pymonetdb
import psycopg2
import os
import regex as re

TABLES = ["dbgen_version", "customer_address", "customer_demographics", "date_dim", "warehouse", "ship_mode", "time_dim", "reason", "income_band", "item", "store", "call_center", "customer", "web_site", "store_returns", "household_demographics", "web_page", "promotion", "catalog_page", "inventory", "catalog_returns", "web_returns", "web_sales", "catalog_sales", "store_sales"]

def exec_sql(cursor, sql_file):
    print(f"\n[INFO] Executing SQL script file: {sql_file}")
    statement = ""
    for line in open(sql_file):
        if re.match(r'--', line):  # ignore sql comment lines
            continue
        if not re.search(r';$', line):  # keep appending lines that don't end in ';'
            statement = statement + line
        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            #print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
            try:
                start_time = time.time()
                cursor.execute(statement)
                end_time = time.time()
                return (end_time - start_time)
            except (mysql.connector.errors.OperationalError, mysql.connector.errors.ProgrammingError) as e:
                print(f"\n[WARN] MySQLError during execute statement \n\tArgs: {str(e.args)}")
            statement = ""

def time_lapsed(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins //60
    mins = mins % 60
    print("Time Lapsed H:M:S={0}:{1}:{2}".format(int(hours),int(mins),sec))

def test_mysql():
    mysql_conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="root",
        port="3306",
        database="tpcds"
    )
    time_taken = {}
    mycursor = mysql_conn.cursor()
    #Load data (ETL) 
    start_time = time.time()
    for table in TABLES:
        os.system(f"sed 's/^|/0|/g;s/||/|0|/g;s/|$/|0/g' -i /var/lib/mysql-files/{table}.dat")
        mycursor.execute(f"LOAD DATA INFILE '/var/lib/mysql-files/{table}.dat' INTO TABLE {table} COLUMNS TERMINATED BY '|' LINES TERMINATED BY '\n';")
    mysql_conn.commit()
    end_time = time.time()
    time_taken["ETL"] = end_time - start_time
    time_lapsed(time_taken["ETL"])
    return

def test_postgresql():
    postgresql_conn = psycopg2.connect(
        database="tpcds",
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        port="5432"
    )
    time_taken = {}
    pcursor = postgresql_conn.cursor()
    #Load data (ETL) 
    start_time = time.time()
    for table in TABLES:
        os.system(f"sed -i 's/|$//' {table}.dat")
        pcursor.execute(f"COPY {table} FROM '/tmp/{table}.dat' DELIMITER '|';")
    postgresql_conn.commit()
    end_time = time.time()
    time_taken["ETL"] = end_time - start_time
    return

def test_monetdb():
    monetdb_conn = pymonetdb.connect(
        username="monetdb",
        password="monetdb",
        hostname="127.0.0.1",
        database="tpcds"
    )
    time_taken = {}
    mcursor = monetdb_conn.cursor()
    #Load data (ETL) 
    start_time = time.time()
    for table in TABLES:
        mcursor.execute(f"COPY INTO {table} FROM '/tmp/{table}.dat' ON CLIENT USING DELIMITERS '|', E'\n', '\"' NULL AS '';")
    monetdb_conn.commit()
    end_time = time.time()
    time_taken["ETL"] = end_time - start_time
    time_lapsed(time_taken["ETL"])
    for i in range(1,100):
        sql_file = f"queries/Default/query{i}.sql"
        time_taken[f"{i}"] = exec_sql(mcursor, sql_file)
        time_lapsed(time_taken[f"{i}"])
    return

def test_tidb():
    tidb_conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="root",
        port="4000",
        database="tpcds"
    )
    time_taken = {}
    tcursor = tidb_conn.cursor()
    #Load data (ETL) 
    start_time = time.time()
    for table in TABLES:
        os.system(f"sed 's/^|/0|/g;s/||/|0|/g;s/|$/|0/g' -i /var/lib/mysql-files/{table}.dat")
        tcursor.execute(f"LOAD DATA INFILE '/var/lib/mysql-files/{table}.dat' INTO TABLE {table} COLUMNS TERMINATED BY '|' LINES TERMINATED BY '\n';")
    tidb_conn.commit()
    end_time = time.time()
    time_taken["ETL"] = end_time - start_time
    return

def test_citus():
    citus_conn = psycopg2.connect(
        database="tpcds",
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        port="9700"
    )
    time_taken = {}
    ccursor = citus_conn.cursor()
    #Load data (ETL) 
    start_time = time.time()
    for table in TABLES:
        os.system(f"sed -i 's/|$//' {table}.dat")
        ccursor.execute(f"LOAD DATA INFILE '/var/lib/mysql-files/{table}.dat' INTO TABLE {table} COLUMNS TERMINATED BY '|' LINES TERMINATED BY '\n';")
    citus_conn.commit()
    end_time = time.time()
    time_taken["ETL"] = end_time - start_time
    return

if __name__ == "__main__":
    print("1. MySQL Test ")
    print("2. Postgreql Test")
    print("3. MonetDB Test")
    print("4. TiDB Test")
    print("5. Citus Test")
    choice = int(input("Select an option: "))
    if (choice==1):
        test_mysql()
    if (choice==2):
        test_postgresql()
    if (choice==3):
        test_monetdb()
    if (choice==4):
        test_tidb()
    if (choice==5):
        test_citus()
