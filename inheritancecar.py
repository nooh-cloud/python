class vehicle:
    def move(self):
        return "Vehicle is moving"
    
class Car(vehicle):
    def honk(self):
        return "Beep Beep"
    
car = Car()
print(car.move())
print(car.honk())
    
