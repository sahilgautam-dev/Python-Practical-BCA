#Q13. Write a program to perform tuple operations and demonstrate immutability
#taking  inputn from user
t = tuple(map(int,input("Enter tuple elemnts:").split()))  

#tuples tuples 
print("origina Tuple:",t)

#Display Tuple
print("original Tuple:", t)

#Accessing elemnts 
print("First elements:",t[0] )

#slicing 
print("sliced Tuple:",  t[1,3])

#concatenTION 
t2  = (100, 200)
new_tuple = t +t2
print("After concatemation:", new_tuple)

#Demonstrating immutability 
print("\n Immutability Demonstration")
try:
    t[0] = 999
except TypeError:
    print("Tuple is imutable, cannot be change ")
