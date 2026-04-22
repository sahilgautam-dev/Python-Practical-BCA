#Q3.Write a program to demonstrate variable assignment and swapping values.
# Q3: Write a program to swap two numbers.

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display original values
print("\nBefore Swapping:")
print("a =", a)
print("b =", b)

# Swapping using third variable
temp = a
a = b
b = temp

# Display swapped values
print("\nAfter Swapping:")
print("a =", a)
print("b =", b)