number = int(input("Enter the size of the list:"))
l1 = []
for i in range(number) :
    elements = int(input("Enter the number of elements:"))
    l1.append(elements)

summ = 0
for j in l1 :
    summ += j 
print(summ)
