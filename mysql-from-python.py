import os
import pymysql

username = os.getenv("C9_USER")

#connect to the database
connection = pymysql.connect(host="localhost", user=username, password="", db="Chinook")

try: #run a query
        with connection.cursor() as cursor:
            rows = cursor.execute("delete from Friends where name = %s;", 'Bob')
            connection.commit()
finally: 
    #close the connection, regardless of whether the above was successful
    connection.close()

"""
BELOW CREATES TABLE AND ADDS ROWS INTO THAT TABLE FOR THIS TO WORK YOU NEED TO ADD "import datetime"
the columns with #'s are the the lines of code 

# cursor.execute("CREATE TABLE IF NOT EXISTS Friends(name char(20),age int, DOB datetime);")
CREATE TABLE WITH 3 COLUMNS FRIENDS AGE AND DATE OF BIRTH

# rows = [("Bob", 21, "1990-02-06 23:04:56"), ("Jim", 56, "1955-05-09 13:34:36"), ("Fred", 100, "1911-09-01 11:14:16")]
THIS CREATES VALUABLES TO BE ADDED INTO THE TABLE

#cursor.executemany("Insert into Friends values (%s, %s, %s);", rows)
THIS ADDS THE VALUE ROW INTO THE TABLE

ADD THIS TO THE "try" function for this to work
"""

"""
BELOW AMENDS DATA IN A TABLE
the columns with #'s are the the lines of code

# with connection.cursor() as cursor:

# rows = [(23, "Bob"), (24, "Jim"), (25, "Fred")]
VALUES TO BE AMENDED

# cursor.executemany("update Friends set age = %s where name = %s;", rows)
CODE TO EXECUTE CHANGE

ADD TO "try" FUNCTION between 
#with connection.cursor() as cursor:
and
# connection.commit()
"""