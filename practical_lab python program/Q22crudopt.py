#Q22 Write a program to perform INSERT, UPDATE, DELETE, and SELECT operations on a database.
import sqlite3

#connect to data base
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

#create table 
cursor.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER, name TEXT)")

#INSERT 
cursor.execute("INSERT INTO student VALUES (1, 'sahil')")
cursor.execute("INSERT INTO student VALUES (2, 'vivek')")

#  UPDATE 
cursor.execute("UPDATE student SET name='Aman' WHERE id=1")

print("\n Data After Update ")
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

# DELETE 
cursor.execute("DELETE FROM student WHERE id=2")

print("\n Data After Delete ")
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

# Save changes
conn.commit()

# Close connection
conn.close()

