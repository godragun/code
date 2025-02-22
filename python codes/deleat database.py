import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mark1"
)
mycursor=mydb.cursor()
mysql='drop database mark1'
mycursor.execute(mysql)
