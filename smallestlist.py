size = int(input("Enter the size of the list:"))
l1 = []
for i in range(size) :
    elements = int(input("Enter the  element:"))
    l1.append(elements)
    
smallest = l1[0]

for i in l1 :
    if i < smallest:
        smallest = i
        
print("Smallest number: ",smallest)