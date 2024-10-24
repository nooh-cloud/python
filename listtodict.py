size = int(input("Enter the size of dict: "))

empt_dict = {}

key = []
value=[]
for i in range(size):
    key1 = input("Enter the key: ")
    value1 = input("Enter the value: ")
    key.append(key1)
    value.append(value1)
    
empt_dict=dict(zip(key,value))

print(empt_dict)

