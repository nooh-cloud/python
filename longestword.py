my_string = input("Enter a sentence to find the longest word: ")


word = my_string.split()


longest_word = ''

for i in word:
    if len(i) > len(longest_word):
       longest_word = i
       
print("The longest word is.",longest_word)


