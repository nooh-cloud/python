def simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time (in years): "))
    
    interest = (principal * rate * time) / 100
    print("The simple interest is:", interest)

simple_interest()
