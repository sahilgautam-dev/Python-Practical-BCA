#Q4. Write a program using if-else to find the largest of three numbers.


# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Finding largest number
if a > b and a > c:
    print("Largest number is:", a)
elif b > a and b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)