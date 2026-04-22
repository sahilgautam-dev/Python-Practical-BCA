# Q5: Write a program to check whether a number is positive, negative, or zero.

# Taking input from user
x = int(input("Enter a number: "))

# Checking the number using nested if
if x >= 0:
    if x == 0:
        print("The number is Zero")
    else:
        print("The number is Positive")
else:
    print("The number is Negative")
    