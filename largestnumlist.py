size = int(input("Enter the size of the list: "))
l1 = []
for i in range(size):
    a = int(input("Enter the elements:"))
    l1.append(a)
print(l1)

largest = 0

for i in l1:
   if i > largest :
       largest = i 
print(largest)
           
