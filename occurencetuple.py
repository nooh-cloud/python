size = int(input("Enter the size of the tuple: "))
l1 = []

for i in range(size):
    elements = input("Enter the elements: ")
    l1.append(elements)
    
find = input("Enter the elements to find the occurence : ")

count = 0

for j in l1 :
    if j == find :
        count += 1
        
print(count)