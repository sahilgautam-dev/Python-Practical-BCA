# Q14: Dictionary operations (add, update, delete)

# creating dictionary 
student = {}

#taking input
n = int(input("how many items: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    student[key] = value

#Display original dictionary 
print("\noriginal Dictionary:", student)

#Add operation 
student["city"] = "Lucknow"
print("\n After adding(city):", student)

#update operation 
key_update = input("\n ENter key update:")
if key_update in student:
    new_value = input("Enter new value:")
    student[key_update] = new_value
    print("After update:", student)

else:
    print("key not found")

#delete operation 
key_delete = input("\n enter key  to delete: ")
if key_delete in student:
    del  student[key_delete]
    print("After Deletion:", student)
else:
    print("key not found")