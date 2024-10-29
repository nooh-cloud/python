def unit(kilometers):
    miles = (kilometers * 0.621371) 
    return miles

kilometers = int(input("Enter the distance in kilometers: "))
print("The distance in miles is : ",unit(kilometers))