def even(number):
    return number % 2 == 0
number = int(input("Enter a number: "))
if even(number):
    print("The number is even.")
else :
    print("The number is odd.")