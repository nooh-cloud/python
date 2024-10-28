empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    empty_dict[key] = value

print("Original Dictionary:", empty_dict)

length_dict = {}
for value in empty_dict.values():
    length_dict.setdefault(len(value), []).append(value)

print("Grouped by Length:", length_dict)
