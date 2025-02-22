import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="salary"
)
mycursor=mydb.cursor()
mycursor.execute("select * from teachar where teachername ='gamge'")
myresult=mycursor.fetchall()#can change all to the specific row value
for x in myresult:
    print (x)
