size = int(input("Enter the size of the tuple: "))
l1 =[]

for i in range(size):
    elements = input("Enter the elements: ")
    l1.append(elements)
    
user_tuple = tuple(l1)


duplicate_tuple = user_tuple

l2 = []

for j in duplicate_tuple:
    if j not in  l2 :
        l2.append(j)
        
unique_tuple = tuple(l2)

print("Tuple without duplicates: ",unique_tuple) 

