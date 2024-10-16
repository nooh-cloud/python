age = int(input('Enter the age:'))

if age >= 0 and age <= 12:
    print('you are a child')
elif age >= 13 and age <= 19:
    print('you are a teen ')
elif age >= 20 and age <= 64 :
    print('you are an adult')
elif age >= 65 :
    print('you are a senior')
else :
    print('invalid')