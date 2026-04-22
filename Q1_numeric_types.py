# Q1. Write a program to demonstrate different numeric data types (int, float) and type conversion

# Taking integer input from user
num1 = int(input("Enter an integer value: "))

# Taking float input from user
num2 = float(input("Enter a float value: "))

# Display original values and their types
print("\n Original Values ")
print("Integer Value:", num1)
print("Type of num1:", type(num1))

print("Float Value:", num2)
print("Type of num2:", type(num2))

# Type conversion
converted_float = float(num1)   # int to float
converted_int = int(num2)       # float to int

# Display converted values and their types
print("\n After Type Conversion ")
print("Converted num1 to float:", converted_float)
print("Type:", type(converted_float))

print("Converted num2 to int:", converted_int)
print("Type:", type(converted_int))
