class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("The number cannot be divisible.")

    
    def display(self):
        print("after addition",self.add())
        print("after substraction",self.sub())
        print("after multiplication",self.multiply())
        print("after division",self.division())
        
p1 = calculator(1,2)

p1.display()