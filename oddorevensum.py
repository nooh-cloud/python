size = int(input("Enter the size of the list: "))
l1 = []
for i in range(size):
    elements = int(input("Enter the elements: "))
    l1.append(elements)
    
oddcount = 0
evencount = 0

for j in l1 :   
    if j % 2 == 0 :
        oddcount += j
        
    else :
        evencount += j
        
print("The odd count is.",oddcount)
print("The even count is.",evencount)