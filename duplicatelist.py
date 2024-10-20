size = int(input("Enter the size of the list:"))
l1 = []
for i in range(size) :
    elements = int(input("Enter the number of elements:"))
    l1.append(elements)
    
duplicate = []

for i in l1 :
    if i not in duplicate :
        duplicate.append(i)
        
print("after removing duplicate:",duplicate)