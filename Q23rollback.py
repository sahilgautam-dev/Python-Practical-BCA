# Q23: Demonstrate commit and rollback
import sqlite3 

#connect database 
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

#creatwe table 
cursor.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER, name TEXT)")

try:
    # Start transaction
    cursor.execute("INSERT INTO student VALUES (3, 'Ravi')")
    cursor.execute("INSERT INTO student VALUES (4, 'Amit')")

    #comit changes 
    conn.comit()
    print("Transaction committed sucessfully!")

except:
    #Rollback if error occurs 
    conn.rollback()
    print("Transaction failed ! Rolled back.")


#display data 
cursor.execute("SELECT*FROM student")
print("\nCurrent Data:")
for row in cursor.fetchall():
    print(row)

#close connection 
conn.close()