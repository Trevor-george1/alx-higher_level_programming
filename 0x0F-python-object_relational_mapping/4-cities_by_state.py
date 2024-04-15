#!/usr/bin/python3
"""script that lists all cities from database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    curr = db.cursor()

    curr.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")

    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()
