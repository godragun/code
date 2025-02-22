import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="salary"
)
mycursor=mydb.cursor()
sql="delete  from teachar where teachername =%s"
tname=("kamal",)
mycursor.execute(sql,tname)
mydb.commit
print (mycursor.rowcount,'records deleted')

