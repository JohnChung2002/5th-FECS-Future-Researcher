import psycopg2

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
                cursor.execute(statement)
            except psycopg2.errors as e:
                print(f"\n[WARN] Postgresql Error during execute statement \n\tArgs: {str(e.args)}")
            statement = ""

conn = psycopg2.connect(
    database="tpcds",
    host="127.0.0.1",
    user="postgres",
    password="postgres",
    port="9700"
)
cursor = conn.cursor()
exec_sql(cursor, "tpcds-citus.sql")