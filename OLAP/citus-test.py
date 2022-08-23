import time
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
            except psycopg2.errors as e:
                print(f"\n[WARN] Postgresql Error during execute statement \n\tArgs: {str(e.args)}")
            statement = ""

def time_lapsed(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins //60
    mins = mins % 60
    print("Time Lapsed H:M:S={0}:{1}:{2}".format(int(hours),int(mins),sec))

def etl_test(conn, cursor):
    #Load data (ETL) 
    start_time = time.time()
    for table in TABLES:
        os.system(f"sed -i 's/|$//' {table}.dat")
        cursor.execute(f"COPY {table} FROM '/tmp/{table}.dat' DELIMITER '|';")
    conn.commit()
    end_time = time.time()
    return (end_time - start_time)

def write_results(name, results):
    with open(f"Citus_{name}.txt", "w") as f:
        for key in results:
            f.write(f"Time taken for {key} query: {time_lapsed(results[key])}\n")

def test_monetdb(query_path):
    conn = psycopg2.connect(
        database="tpcds",
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        port="5432"
    )
    time_taken = {}
    cursor = conn.cursor()
    time_taken["ETL"] = etl_test(conn, cursor)
    time_lapsed(time_taken["ETL"])
    for i in range(1,100):
        sql_file = f"{query_path}/query{i}.sql"
        time_taken[f"{i}"] = exec_sql(cursor, sql_file)
        time_lapsed(time_taken[f"{i}"])
    return time_taken



if __name__ == "__main__":
    option = {1 : "30GB", 2 : "100GB"}
    print("---Citus TPC-DS Test---")
    for key in option:
        print(f"{key}. {option[key]}")
    choice = int(input("Select an option: "))
    results = test_monetdb(f"queries/Netezza/{option[choice]}")
    write_results(option[choice], results)