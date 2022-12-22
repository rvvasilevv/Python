import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123brawo123",
  database="pythondb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM imenta WHERE id <10 ")
myresult=mycursor.fetchall()
for x in myresult:
  print(x)