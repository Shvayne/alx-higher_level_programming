#!/usr/bin/python3
"""a script that takes in the name of a
    state as an argument and lists all cities of 
    that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
            )
    cursor = db.cursor()
    query = """
    SELECT cities.name\
    FROM cities
    JOIN states ON cities.state_id = states.id\
    WHERE states.name LIKE BINARY %(state_name)s\
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print (row)

    cursor.close()
    db.close()

