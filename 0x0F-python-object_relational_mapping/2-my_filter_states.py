#!/usr/bin/python3
'''
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
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
                   WHERE Binary name='{}'
                   ORDER BY id
                   '''.format(state_search))
    q_rows = cursor.fetchall()
    for row in q_rows:
        print(row)
    cursor.close()
    connection.close()
