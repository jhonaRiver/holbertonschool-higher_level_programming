#!/usr/bin/python3
'''
script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    connection = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    q_rows = cursor.fetchall()
    for row in q_rows:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    connection.close()
