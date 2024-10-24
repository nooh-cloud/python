size = int(input("Enter the size of the set:"))
l1 =[]

for i in range(size):
    elements = int(input("Enter the elements: "))
    l1.append(elements)
    
    
user_set = set(l1)

order_list = []

for  i in user_set:
    if i not in l1:
        order_list.append(user_set)
        
print(user_set)