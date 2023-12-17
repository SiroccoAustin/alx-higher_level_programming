#!/usr/bin/python3

"""Filter the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = conn.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id")
    rows = c.fetchall()
    for eachRow in rows:
        print(eachRow)
    c.close()
    conn.close()
