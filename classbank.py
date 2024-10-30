class Bankacc:
    def __init__(self,accno,balance = 0):
        self.accno = accno
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(amount)
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance.")
        else:
            self.balance -= amount
            print("withdraw amount: ",amount)
    
    def display(self):
        print("Your account balance: ",self.balance)
        
p1 = Bankacc(12345)
p1.deposit(1000)
p1.withdraw(500)
p1.display()
        
