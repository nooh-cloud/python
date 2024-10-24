empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    empty_dict[key] = value
    
print(empty_dict)


changekey = input("Enter the key that wants to update: ")

if changekey in empty_dict:
    changevalue = input("Enter the value to update: ")
    empty_dict[changekey] = changevalue
else:
    print("key not found.")
    

print(empty_dict)    