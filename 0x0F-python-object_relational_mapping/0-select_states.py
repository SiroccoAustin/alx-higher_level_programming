#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for eachRow in rows:
        print(eachRow)
    c.close()
    conn.close()
