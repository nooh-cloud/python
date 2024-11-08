string1 = input("Enter the string 1: ")
string2 = input("Enter the string 2: ")

    
if sorted(string1) == sorted(string2):
    print("This is a anagram")
else:
    print("This is not anagram")