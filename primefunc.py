def prime():
    number = int(input("Enter a number: "))
    if number <= 1:
        print("The number is not prime")
        return
    
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            print("The number is not prime.")
            return
    print("The number is prime.")
    
prime()