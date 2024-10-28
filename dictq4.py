empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    empty_dict[key] = value
    
print(empty_dict)

threshold = int(input("Enter the threshold: "))

filtered_data = {key: value for key,value in empty_dict.items() if value >= threshold}

print("filtered dictionary:",filtered_data)