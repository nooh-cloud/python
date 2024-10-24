fruits = {
    "Apple": 120,
    "Banana": 40,
    "Orange": 60
}

new_fruit = input("Enter the name of the fruit: ")
price = int(input("Enter the price of the fruit: "))

fruits[new_fruit] = price
print("Updated Dictionary:", fruits)
