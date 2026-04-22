#Q16. Write functions to organize a program that performs basic operations on strings and lists
#function for string opeerations 
def string_operations(text):
    print("\n Streing Operations ")
    print("Original string", text)
    print(" length :",len(text))
    print("uppercase:",text.upper())
    print("Reversed", text[::-1])

#function for list operations 
def list_operations(nums):
    print("\n LIst operation")
    print("List", nums)
    print("Length:", len(nums))
    print("Sum:", sum(nums))
    print("Maimum:", max(nums))
    print("Minimum", min(nums))

#main program 
text = input("Enter a string ")
nums = list(map(int, input("Enter list elements:").split()))


#caling functions 
string_operations(text)
list_operations(nums)