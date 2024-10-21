size = int(input("Enter the size of the tuple: "))
l1 =[]

for i in range(size):
    elements = input("Enter the elements: ")
    l1.append(elements)
    
user_tuple = tuple(l1)

number = input("Enter the number to find the index: ")

index = -1

for j in range(size):
    if l1[j] == number:
       index = j
       break
   
if index != -1 :
    print("number  found at position  ",j)
else :
    print("The numbe not found.")