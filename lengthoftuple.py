size = int(input("Enter the size of the tuple: "))
l1 =[]

for i in range(size):
    elements = input("Enter the elements: ")
    l1.append(elements)
    
user_tuple = tuple(l1)


tuple_length = 0

for j in user_tuple:
    tuple_length += 1 


print("Length of the tuple:", tuple_length)