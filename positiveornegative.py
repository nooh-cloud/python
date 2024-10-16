a = int(input('enter a number:'))
if a > 0:
    print(a,'is a positive number')
    if a % 2 == 0 :
        print(a,'is even number')
    else :
        print(a,'is odd number')
        
elif a < 0:
    print(a,'is a negative number')
else :
    print(a,'is zero')