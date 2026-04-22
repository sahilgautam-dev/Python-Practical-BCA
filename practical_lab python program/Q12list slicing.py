#Q12. Write a program to demonstrate list slicing and list manipulation.
#taking list input from user
nums = list(map(int, input("Enter the elements:").split()))
 #list slicing 
print("\n List Slicing")
print("original List", nums)
print("First 3 element ",nums [0:3])
print("last 2 elements:", nums[-2:])

#list manipulation 
print("\n  List Manipulation")

#append 
nums.append(110)
print("after append", nums)
#inert 
nums.insert(1,55)
print("after insert", nums)
#remove
nums.remove(nums[2])
print("After remove:", nums)
#update
nums[0] = 999
print("After update:", nums)
