import time
import psycopg2
import os
import regex as re

TABLES = ["dbgen_version", "customer_address", "customer_demographics", "date_dim", "warehouse", "ship_mode", "time_dim", "reason", "income_band", "item", "store", "call_center", "customer", "web_site", "store_returns", "household_demographics", "web_page", "promotion", "catalog_page", "inventory", "catalog_returns", "web_returns", "web_sales", "catalog_sales", "store_sales"]
SKIP = [1]

def exec_sql(cursor, sql_file):
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
                print(f"\n[INFO] Executing SQL script file: {sql_file}")
                start_time = time.time()
                cursor.execute(statement)
                end_time = time.time()
                return (end_time - start_time)
            except psycopg2.Error as e:
                print(f"\n[WARN] Postgresql Error during execute statement \n\tArgs: {str(e.args)}")
                return 0

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins //60
    mins = mins % 60
    return ("{0}:{1}:{2}".format(int(hours),int(mins),sec))

def etl_test(conn, cursor):
    #Load data (ETL) 
    start_time = time.time()
    for table in TABLES:
        print(f"[Info] Inserting {table}")
        os.system(f"sudo -u postgres psql -p 9700 -c \"\COPY {table} FROM '/tmp/{table}.dat' WITH DELIMITER AS '|' NULL AS '';\"")
    os.system(f"sudo -u postgres psql -p 9700 -c 'VACUUM VERBOSE ANALYZE;'")
    end_time = time.time()
    return (end_time - start_time)

def write_results(name, results):
    with open(f"Citus_{name}.txt", "w") as f:
        for key in results:
            f.write(f"Time taken for {key} query: {time_convert(results[key])}\n")

def test_citus():
    conn = psycopg2.connect(
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        port="9700"
    )
    time_taken = {}
    cursor = conn.cursor()
    time_taken["ETL"] = etl_test(conn, cursor)
    print(f"Time Lapsed H:M:S={time_convert(time_taken['ETL'])}")
    for i in range(1,100):
        if (i in SKIP):
            time_taken[f"{i}"] = 0
            continue
        sql_file = f"queries/Postgresql/query{i}.sql"
        time_taken[f"{i}"] = exec_sql(cursor, sql_file)
        print(f"Time Lapsed H:M:S={time_convert(time_taken[f'{i}'])}")
    return time_taken

if __name__ == "__main__":
    option = {1 : "10GB", 2 : "30GB", 3 : "100GB"}
    print("---Citus TPC-DS Test---")
    for key in option:
        print(f"{key}. {option[key]}")
    choice = int(input("Select an option: "))
    if choice in option.keys():
        results = test_citus()
        write_results(option[choice], results)
    else:
        print("Invalid selection. Exiting...")