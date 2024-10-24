size = int(input("Enter the size of set: "))
l1 = []

for i in range(size):
    elements = int(input("Enter the elements: "))
    l1.append(elements)
    
user_set = set(l1)


maximum_value = 0

for i in user_set:
    if maximum_value == 0 or i > maximum_value:
     maximum_value = i
    
print(maximum_value)
    
        
