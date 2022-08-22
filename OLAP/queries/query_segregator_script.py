import time

with open("query_0.sql", "r") as f:
    num = 1
    lines = f.readlines()
    for l in lines:
        if (l=="\n"):
            pass
        else:
            with open(f"query{num}.sql", "a+") as w:
                w.write(l)
                if (l == f"-- end query {num} in stream 0 using template query{num}.tpl\n"):
                    num += 1
            time.sleep(0.05)
