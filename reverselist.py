n = int(input("Enter the size of list:"))
l1 = []

for i in range(n) :
    elements = int(input("Enter the elements:"))
    l1.append(elements)

reversedlist = []   
 
while n -1 >= 0 :
    reversedlist.append(l1[n-1])
    n -= 1

print(reversedlist)