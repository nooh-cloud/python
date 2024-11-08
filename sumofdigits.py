number = int(input("Enter a number: ")) 
summ = 0

while number > 0:
    digit = number % 10 
    summ += digit  
    number = number // 10 
print("Sum of the digits:", summ)
