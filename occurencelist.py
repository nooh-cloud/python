size = int(input("Enter the size of the list:"))
l1 = []
for i in range(size):
    elements = int(input("Enter the elements:"))
    l1.append(elements)

occurence = int(input("Enter the number to find  occurence:"))

count = 0    

for j in l1:
    if j == occurence :
       count += 1
       
print(count)
    

