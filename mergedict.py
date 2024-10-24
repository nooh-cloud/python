empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    empty_dict[key] = value
    
print(empty_dict)


empty_dict2 = {}

size2 = int(input("Enter the size of dict2: "))

for j in range(size2):
    key2 = input("Enter the key: ")
    value2 = input("Enter the value: ")
    empty_dict2[key2] = value2
    
print(empty_dict2)

empty_dict.update(empty_dict2)

print("After merging the dict: ",empty_dict)