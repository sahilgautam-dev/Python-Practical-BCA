#Q20. Write a program to demonstrate file pointer operations using seek().

#create file and write data
file = open("data.txt","w")
file.write("Hello world")
file.close()

#open file in read mode 
file =open("data.txt","r")

#Read first 5 characters 
print("First read", file.read(5))

#move pointer to begining 
file.seek(0)
print("After seek(0):", file.read(5))

#move pointer to position 6
file.seek(6)
print("After seek(6):", file.read())

#close file
file.close()
























