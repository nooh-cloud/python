numbers = int(input("Enter the size of the list:"))
l1 = []
for i in range(numbers):
    elements = int(input("Enter the elements:"))
    l1.append(elements)

key = int(input("Enter the element to check:"))

found = False
for j in l1 :
    if j == key :
        found = True
        break
if found == True :
    print("the element is in the list")
else :
    print("the element is not in the list.")
