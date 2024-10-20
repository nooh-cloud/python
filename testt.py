size = int(input("Enter the size: "))
l1 =[]

for i in  range(size) :
    elements = input("Enter the elemets: ")
    l1.append(elements)
    
reversedlist = []

while size -1 >= 0 :
    reversedlist.append(l1(size -1))
    size -= 1
    
    
print("The reversed list: ",reversedlist)