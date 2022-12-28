import mysql.connector

basadani=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123brawo123',
    database='pythondb'
)
cursor=basadani.cursor()
cursor.execute("INSERT INTO imena(id,name,godini) VALUES(25,'RADKO',222)")
basadani.commit()


