# Q8: Write a program to compute sum of first N natural numbers using while loop.

# Taking input from user
num = int(input("Enter the number: "))

# Initialization
total = 0
i = 1

# While loop
while i <= num:
    total = total + i
    i = i + 1

# Display result
print("Sum of first", num, "natural numbers is:", total)