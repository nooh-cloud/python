empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    empty_dict[key] = value
    
print(empty_dict)

threshold = int(input("Enter the value: "))

filtered_data = {key: value for key,value in empty_dict.items() if value % 2 != 0 }

print("dictionary after removing even values:",filtered_data)