#Q17. Write a program to read contents of a file using read(), readline(), and readlines().

#open file in read mode 
file = open("data.text", "r")

#using read()
print("using read()")
content = file.read()
print(content)

#reset pointer to begining 
file.seek(0)

#using readline()
print("\n Using readline()")
line = file.readline()
print(line)

#reset pointer again 
file.seek(0)

#using readlines()
print("\n Usingreadlines()")
lines = file.readlines()
print(lines)

#close file 
file.close()