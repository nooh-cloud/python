def palindrome():
    string = input("Enter a word to check palindrome: ")
    if string == string[::-1]:
        print("This is a palindrome.")
    else:
        print("This is not palindrome.")
        
palindrome()