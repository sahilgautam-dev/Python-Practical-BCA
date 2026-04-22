#Q18. Write a program to write and append data to a file.

# writing data to file 
file = open("data.txt", "w")
file.write("Hello World\n")
file.write("Python Programming\n")
file.close()

print("Data written successfully!")

# Appending data to file
file = open("data.txt", "a")
file.write("This is appended line\n")
file.close()

print("Data appended successfully!")