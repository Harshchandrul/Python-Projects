import mysql.connector as k

connection = k.connect(host="localhost", user="root", password="123456")
cursor = connection.cursor()
cursor.execute("CREATE DATABASE rough")
cursor.execute("USE rough")

connection.commit()
connection.close()
