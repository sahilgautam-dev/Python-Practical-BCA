# Q6: Write a program to print multiplication table using for loop.

# Taking input from user
num = int(input("Enter a number: "))

# Printing table
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")