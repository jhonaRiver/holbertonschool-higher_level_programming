#!/usr/bin/python3
'''
script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time, write one that
is safe from MySQL injections
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_search = argv[4]

    connection = MySQLdb.connect(host='localhost', port=3306, user=user,
                                 passwd=password, db=db_name)
    cursor = connection.cursor()
    cursor.execute('''
                   SELECT * FROM states
                   WHERE name= %(state_search)s
                   ORDER BY id
                   ''', {'state_search': state_search})
    q_rows = cursor.fetchall()
    for row in q_rows:
        print(row)
    cursor.close()
    connection.close()
