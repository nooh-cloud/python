string = input('Enter a word:')

vowels = "AEIOUaeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1
        
print(f"the number of vowels in the word is : {count}")