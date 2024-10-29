def vowels():
    string = input("Enter a word: ")
    vowels = "AEIOUaeiou"
    
    count = 0
    
    for  i in string:
        if i in vowels:
            count += 1
            
    print("The vowels in the word are: ",count)
    
vowels()