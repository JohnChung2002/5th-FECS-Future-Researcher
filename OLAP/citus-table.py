import os
import regex as re

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
            os.system(f"sudo -u postgres psql -p 9700 -c \"{statement}\"")
            statement = ""

exec_sql("tpcds-citus.sql")