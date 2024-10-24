empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    empty_dict[key] = value

print(empty_dict)
    
key1 = input("Enter the key to add in dict: ")
value1 = input("Enter the value to add in dict: ")

empty_dict[key1] = value1

print(empty_dict)