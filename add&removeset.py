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



elementt = input("Enter the element to add in set1: ")
user_set1.add(elementt)
print("set1 after adding the element: ",user_set1)


element = input("Enter the element to remove from set2: ")
if element in user_set2:
    user_set2.remove(element)
    print("set2 after removing the element: ",user_set2)
else:
    print("element not found in user set2.")
