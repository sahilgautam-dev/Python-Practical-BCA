#Q24. Write a program to handle exceptions using try-except blocks.
try:
    # Taking input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except Exception as e:
    print("Some error occurred:", e)