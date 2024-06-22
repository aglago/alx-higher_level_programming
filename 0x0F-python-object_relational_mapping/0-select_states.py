#!/usr/bin/python3

import MySQLdb
import sys

'''
This script connects to a
MySQL database and retrieves
all records from the 'states'
table.
'''

if __name__ == '__main__':
    hostname = 'localhost'
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(
        host=hostname,
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    cursor = conn.cursor()

    # query = 'SELECT * FROM states'

    cursor.execute('SELECT * FROM states')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
