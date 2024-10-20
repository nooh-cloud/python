list1 = int(input("Enter the size of list1:"))
l1 = []

for i in range(list1) :
    elements = int(input("Enter the elements of list1:"))
    l1.append(elements)
    
list2 = int(input("Enter the number of list2: "))
l2 = []

for j in range(list2) :
    elements2 = int(input("Enter the elements of list2: "))
    l2.append(elements2)
    
    
mergedlist = l1 + l2
print("the merged list is :",mergedlist)