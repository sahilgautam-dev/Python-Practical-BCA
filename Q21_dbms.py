#Q21. Write a program to connect to a database and create a table.
import sqlite3

#connect to database (cretae file if not exists)
conn = sqlite3.connect("student.db")

#cerate cursor
cursor = conn.cursor()

#create table 
cursor.execute("CREATE TABLE IF NOT EXISTS student (ID INTEGER, name TEXT)")

#save chnages 
conn.close()

print("Database connected and table created successfully!:")