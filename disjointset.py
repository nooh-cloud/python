size = int(input("Enter the size of the set1: "))
l1 = []

for i in range(size):
    elements1 = input("Enter the elements of set1: ")
    l1.append(elements1)
    
user_set1 = set(l1)


size2 = int(input("Enter the size of the set2: "))
l2 = []

for j in range(size2):
    elements2 = input("Enter the elements of set2: ")
    l2.append(elements2)
    
user_set2 = set(l2)

disjoint = True
for i in user_set1:
    if i in user_set2:
        disjoint = False
        break
    
if disjoint:
    print("The sets are disjoint.",disjoint)
else:
    print("The sets are not disjoint.")
    