size = int(input("Enter the size of the tuple: "))
l1 =[]

for i in range(size):
    elements = input("Enter the elements: ")
    l1.append(elements)
    
user_tuple = tuple(l1)


first_element = user_tuple[0]
last_element = user_tuple[-1]

print("The tuple is : ",user_tuple)
print("The first element is : ",first_element)
print("The last element is : ",last_element)