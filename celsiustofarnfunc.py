def temp(celsius):
    farnhiet = (celsius * 9/5) + 32
    return farnhiet

celsius = float(input("Enter the temp in celsius: "))
print("The temp in farenhiet is : ",temp(celsius))