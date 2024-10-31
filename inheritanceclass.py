class animal:
    def speak(self):
        return "Animal sound"
    
class Dog(animal):
    def bark(self):
        return "Wolf"
    
dog = Dog()
print(dog.speak())
print(dog.bark())