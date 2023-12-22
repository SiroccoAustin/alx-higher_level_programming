#!/usr/bin/python3

"""List all cities"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("""SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE states.name=%s""", (sys.argv[4],))
    rows = c.fetchall()
    my_cities = list(row[0] for row in rows)
    print(*my_cities, sep=", ")
    c.close()
    conn.close()
