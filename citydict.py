empty_dict = {}

size = int(input("Enter the size of dict: "))

for i in range(size):
    key = input("Enter the  key: ")
    value = input("Enter the value: ")
    empty_dict[key] = value
    

city = input("Enter the city name: ")
if city in empty_dict:
    print(empty_dict[city])
else:
    print("city not found.")