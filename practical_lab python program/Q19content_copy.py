#Q19. Write a program to copy contents of one file to another
#open soruce file in read mode 
source = open("data.txt", "r")

#read content 
content = source.read()

#open destination file in write mode 
destination = open("Q19copy.txt","w")

#writeb cotent to new file 
destination.write(content)

#close both files
source.close()
destination.close()

print("file copied sucessfully!:")