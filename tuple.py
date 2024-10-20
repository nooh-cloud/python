a = ("apple","mango","orange")
b= list(a)
b[2] = "hello"
a = tuple(b) 
print("this is a tuple",tuple(a))