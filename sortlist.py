size = int(input("enter the size of the list:"))
l1 = []
for i in range(size) :
    elements = int(input("Enter the elements:"))
    l1.append(elements)

for j in range(size):
    
    for k in range(size - 1):
        if l1[k] > l1[k + 1] :
            l1[k] , l1[k + 1] = l1[k + 1] , l1[k]
            
print(l1) 
    
    
        
