#!/usr/bin/python3

"""SQL Injection"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    my_spot = sys.argv[4]
    c = conn.cursor()
    c.execute("SELECT * FROM states WHERE name = %s", (my_spot, ))
    rows = c.fetchall()
    for eachRow in rows:
        print(eachRow)
    c.close()
    conn.close()
