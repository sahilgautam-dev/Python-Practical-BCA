#Q25 Q25. Write a program demonstrating multiple exceptions handling.


#  Multiple exception handling

try:
    # Taking input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Division
    result = num1 / num2
    print("Result:", result)

    # List access (to generate IndexError)
    my_list = [10, 20, 30]
    index = int(input("Enter index (0-2): "))
    print("Element:", my_list[index])

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except IndexError:
    print("Error: Index out of range!")

except Exception as e:
    print("Some unexpected error occurred:", e)