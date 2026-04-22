# Q7: Iterate through string, list, and dictionary using loops

# String input
name = input("Enter the name: ")
for ch in name:
    print(ch)

# List input
numbers = list(map(int, input("Enter the numbers: ").split()))
for num in numbers:
    print(num)

# Dictionary input
my_dict = {}
n = int(input("How many items: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

for key, value in my_dict.items():
    print(key, ":", value)

# Display types and data
print(type(name))
print(numbers)
print(my_dict)