#!/usr/bin/python3

"""Lists all states in the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit(1)

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for eachRow in rows:
        print(eachRow)
    c.close()
    conn.close()
