class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        

    def brake(self, amount):
        self.speed = max(0, self.speed - amount) 
        

    def display(self):
         print(f"Car Make: {self.make}, Model: {self.model}, Speed: {self.speed} km/h")
        
p1 = Car(2006,"ford")
p1.accelerate(30)
p1.brake(5)
p1.display()