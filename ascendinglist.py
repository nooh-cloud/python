size = int(input("Enter the size of the list:"))
l1 = []
for i in range(size) :
    elements = int(input("Enter the  element:"))
    l1.append(elements)
    
sortedd = True

for j in range(size-1) :
    if l1[j] > l1[j + 1] :
        sortedd = False 
        break
    
if sortedd == True :
    print("The list is sorted.",l1)
else :
    print("This list is not sorted:",l1)
    