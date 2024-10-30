# class hello:
#     name = "nooh"
#     age = 18
#     def myfun(self):
#         print(self.name,self.age)
# p1 = hello()
# p1.myfun()
        
        
class Student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print(self.id,self.name,self.age)
        
p1 = Student(1,"nooh",25)
p1.display()
        
        
