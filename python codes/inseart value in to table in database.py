import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="salary"
)
mycursor=mydb.cursor()
sql= "insert into teachar (teacharid, teachername ,address) values (%s,%s,%s)"
val1=("t003","nimal","rathnapura")
sql= "insert into teachar (teacharid, teachername ,address) values (%s,%s,%s)"
val2=("t004","kasun","rathnapura")
sql= "insert into teachar (teacharid, teachername ,address) values (%s,%s,%s)"
val3=("t005","chamath","rathnapura")
mycursor.execute(sql,val1,val2,val3)

mydb.commit()
print (mycursor.rowcount,'record inserted')
