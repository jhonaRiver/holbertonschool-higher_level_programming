#!/usr/bin/python3
'''
script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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
                   SELECT name FROM cities
                   WHERE state_id = (
                        SELECT id FROM states
                        WHERE name = %(state_search)s )
                   ORDER BY id
                   ''', {'state_search': state_search})
    q_rows = cursor.fetchall()
    li = [row[0] for row in q_rows]
    print(', '.join(li))
    cursor.close()
    connection.close()
