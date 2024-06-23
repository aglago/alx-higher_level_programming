#!/usr/bin/python3

"""
This script connects to a MySQL database
and retrieves all records from the 'cities' table.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    host = "localhost"
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=3306
    )

    cursor = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name AS state FROM cities JOIN states ON cities.state_id = states.id LIMIT 15"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
