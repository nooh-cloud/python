empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    empty_dict[key] = value
    
print(empty_dict)

check = input("Enter the key to check: ")

if check in empty_dict:
    print("The key is found in dict.")
else:
    print("key not found in dict.")