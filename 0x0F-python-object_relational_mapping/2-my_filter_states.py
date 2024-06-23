#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the 
states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb
if __name__ == "__main__":
  mysql_username = sys.argv[1]
  mysql_password = sys.argv[2]
  db_name = sys.argv[3]
  db = MySQLdb.connect(
         host="localhost",
         port=3306,
         user=mysql_username,
         passwd=mysql_username,
         db = db_name
  )
  cursor = db.cursor()
  cursor.execute("")
  row = cursor.fetchall()


  
