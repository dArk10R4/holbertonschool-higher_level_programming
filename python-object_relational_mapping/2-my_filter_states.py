#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa with a name matching by arg
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=sys.argv[1], password=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
