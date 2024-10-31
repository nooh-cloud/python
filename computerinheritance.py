class Computer:
    def hello(self):
        return "Computing"
    
class Laptop(Computer):
    def por(self):
        return "Laptop is portable."
    
lap = Laptop()

print(lap.hello())
print(lap.por())