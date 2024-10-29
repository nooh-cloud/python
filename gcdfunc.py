def gcd():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    while b:
        a, b = b, a % b

    print("The GCD of the two numbers is:", a)

gcd()
