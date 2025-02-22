import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="salary"
)
mycursor=mydb.cursor()
mycursor.execute("create table teachar(teacharid varchar(5),teachername varchar(10),address varchar(20))")
