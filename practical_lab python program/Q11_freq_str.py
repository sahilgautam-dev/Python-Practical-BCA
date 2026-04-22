# Q11: Count frequency of characters in a string

# Taking input from user
text = input("Enter a string:")
# Dictionary to store frequency
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch] = 1

# Display result
print("\n Character Frequency:")
for key, value in freq.items():
    print(key, ":", value)