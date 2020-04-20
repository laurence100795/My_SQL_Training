import os
import pymysql

username = os.getenv("C9_USER")

#connect to the database
connection = pymysql.connect(host="localhost", user=username, password="", db="Chinook")


try: #run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally: #close the connection, regardless of whether the above was successful
    connection.close()