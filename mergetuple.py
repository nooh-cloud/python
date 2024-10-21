size = int(input("Enter the size of the tuple: "))
l1 =[]

for i in range(size):
    elements = input("Enter the elements: ")
    l1.append(elements)
    
user_tuple = tuple(l1)


sizeoftuple2 = int(input("Enter the size of the tuple: "))
l2 =[]

for j in range(sizeoftuple2):
    elementss = input("Enter the elements of the tuple you want to merge: ")
    l2.append(elementss)
    
user_tuple2 = tuple(l2)


merged_tuple = (*user_tuple,*user_tuple2)
print(merged_tuple)
