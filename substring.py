string = "I love Python programming"
substring = "Python"

if substring in string:
    print(f"'{substring}' exists in the string.")
else:
    print(f"'{substring}' does not exist in the string.")


removed_substring = string.replace(substring, "")
print(removed_substring)


