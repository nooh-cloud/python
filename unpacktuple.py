size = int(input("Enter the size of the tuple: "))
l1 =[]

for i in range(size):
    elements = input("Enter the elements: ")
    l1.append(elements)
    
user_tuple = tuple(l1)


a, b, c, d = user_tuple[:4] 
    
print("First element:", a)
print("Second element:", b)
print("Third element:", c)
print("Fourth element:", d)