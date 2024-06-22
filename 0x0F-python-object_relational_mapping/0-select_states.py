#!/usr/bin/python3

import MySQLdb
import sys

'''
This script connects to a
MySQL database and retrieves
all records from the 'states'
table.
'''

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = conn.cursor()

    # query = 'SELECT * FROM states'

    cursor.execute("SELECT * FROM states")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
