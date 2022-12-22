import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123brawo123",
  database="pythondb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO imenta(id,name,city) VALUES (1,'Georgi','Sofia')"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount)
