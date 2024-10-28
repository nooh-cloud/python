empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))  
    empty_dict[key] = value

print("Dictionary:", empty_dict)

values_list = list(empty_dict.values())
frequent_value = max(values_list, key=values_list.count)
print("Most frequent value:", frequent_value)
