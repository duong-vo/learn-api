import pymysql

# establish a connection to the database
conn = pymysql.connect(
    host='sql5.freesqldatabase.com',
    database='sql5528137',
    user='sql5528137',
    password='l5Fmqx2StM',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

sql_query = """ CREATE TABLE name (
                    id integer PRIMARY KEY,
                    name text NOT NULL,
                    age text NOT NULL            
                ) """

cursor.execute(sql_query)
conn.close()