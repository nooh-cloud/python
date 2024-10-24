empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    empty_dict[key] = value
    
print(empty_dict)


key1 = input("Enter the key to delete: ")
if key1 in empty_dict:
    del empty_dict[key1]
else:
    print("Key not found in dict.")
    
print(empty_dict)