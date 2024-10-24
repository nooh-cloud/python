empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the key: ")
    value = int(input("Enter the value: "))
    empty_dict[key] = value
    
print(empty_dict)

summ = 0

for value in empty_dict.values():
    summ += value
    
print("sum of the dict is : ",summ)
