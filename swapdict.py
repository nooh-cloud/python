empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    empty_dict[key] = value

print("Original Dictionary:", empty_dict)

swapped_dict = {value: key for key, value in empty_dict.items()}
print("Swapped Dictionary:", swapped_dict)
