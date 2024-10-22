size = int(input("Enter the size of set: "))
l1 = []

for i in range(size):
    elements = int(input("Enter the elements: "))
    l1.append(elements)
    
user_set = set(l1)


size2 = int(input("Enter the size of set: "))
l2 = []

for j in range(size2):
    elements2 = int(input("Enter the elements: "))
    l2.append(elements2)
    
user_set2 = set(l2)


set3 = user_set.union(user_set2)
print("The union of the given sets are: ",set3)


set4 = user_set.intersection(user_set2)
print("The intersection of the given sets are: ",set4)

set5 = user_set.difference(user_set2)
print("The difference of the given sets are: ",set5)