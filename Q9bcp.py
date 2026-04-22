# Q9: Demonstrate use of break, continue, and pass in loops

#  BREAK
print(" Break Example ")
for i in range(1, 6):
    if i == 3:
        break   # loop stops when i = 3
    print(i)

#  CONTINUE 
print("\n Continue Example ")
for i in range(1, 6):
    if i == 3:
        continue   # skip when i = 3
    print(i)

#  PASS 
print("\n Pass Example ")
for i in range(1, 6):
    if i == 3:
        pass   # does nothing
    print(i)