size = int(input("Enter the size of list:"))
l1 = []

for i in range(size):
    elements = int(input("Enter the elements:"))
    l1.append(elements)
    
number = int(input("Enter the number to find the index:"))
    
index = -1

for j in range(size) :
    if l1[j] == number :
        index = j
        break
    
if index != -1 :
    print("number found at the position :",j)        
else :
    print("number not found.")