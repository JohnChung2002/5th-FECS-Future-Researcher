import psycopg2
import os

def exec_sql(sql_file):
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
                os.system(f"sudo -u postgres psql -p 9700 -c \"{statement}\"")
            except psycopg2.Error as e:
                print(f"\n[WARN] Postgresql Error during execute statement \n\tArgs: {str(e.args)}")
            statement = ""

exec_sql(cursor, "tpcds-citus.sql")