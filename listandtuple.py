size = int(input("Enter the size of the tuple: "))
l1 =[]

for i in range(size):
    elements = input("Enter the elements: ")
    l1.append(elements)
    
user_tuple = tuple(l1)


print("This is the original list: ",l1)
print("This is the resulting tuple: ",user_tuple)