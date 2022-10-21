# import pymysql

# # establish a connection to the database
# conn = pymysql.connect(
#     host='sql5.freesqldatabase.com',
#     database='sql5528137',
#     user='sql5528137',
#     password='l5Fmqx2StM',
#     charser='utf8m4',
#     cursorclass=pymysql.cursor.DictCursor

# )

# cursor = conn.cursor()

# sql_query = """ CREATE TABLE name (
#                     id integer PRIMARY KEY,
#                     name text NOT NULL,
#                     age text NOT NULL            
#                 ) """

# cursor.execute(sql_query)
# conn.close()

import sqlite3

conn = sqlite3.connect("names.sqlite")

cursor = conn.cursor()

sql_query = """ CREATE TABLE name (
                    id integer PRIMARY KEY,
                    name text NOT NULL,
                    age text NOT NULL            
                ) """

cursor.execute(sql_query)
conn.close()