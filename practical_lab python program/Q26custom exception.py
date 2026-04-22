#Q26. Write a program using finally and custom exceptions.
try:
    num = int(input("Enter a positive number: "))

    #custom exception 
    if num<0:
        raise Exception("Negative number not allowed!")
    print("you entered:", num)

except Exception as e :
    print("Error", e) 

finally:
    print("this block always executes!")   