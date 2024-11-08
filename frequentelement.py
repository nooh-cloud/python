size = int(input("Enter the size of the list: "))
l1 = []

for i in range(size):
    elements = int(input("Enter the elements: "))
    l1.append(elements)
  
if len(l1) > 0:
    frequent_value = max(set(l1),key=l1.count)
    print("Most frequent value:",frequent_value)  
    
       
