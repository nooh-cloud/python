size = int(input("Enter the size of the set: "))
l1 = []

for i in range(size):
    elements = int(input("Enter the elements of set: "))
    l1.append(elements)
    
user_set = set(l1)


size2 = int(input("Enter the size of the set2: "))
l2 = []

for j in range(size2):
    elementss = int(input("Enter the elements of set2: "))
    l2.append(elementss)
    
user_set2 = set(l2)


user_set.difference_update(user_set2)

print(user_set)