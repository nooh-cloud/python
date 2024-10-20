number = int(input("Enter the size of the list:"))
l1 = []
for i in range(number):
    elements = int(input("Enter the elements:"))
    l1.append(elements)
remove = int(input("Enter the element to remove:"))

newlist = []

for j in l1:
    if j != remove :
        newlist.append(j)

k = len(l1)
m = len(newlist)

if k == m :
    print("Element is not found in the list.")

else :
    print("element removed",newlist)

    
