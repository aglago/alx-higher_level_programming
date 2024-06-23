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
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=db,
        port=3306
    )

    cursor = conn.cursor()

    query = "SELECT cities.id, cities.name AS cities_name, states.name AS states_name FROM cities INNER JOIN states on cities.state_id = states.id WHERE states.name = %s"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    cities = [row[1] for row in rows]
    print(*cities, sep=", ")

    cursor.close()
    conn.close()
