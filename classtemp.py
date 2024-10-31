class TemperatureConverter:
    def __init__(self, temperature):
        self.temperature = temperature

    def celsius_to_fahrenheit(self):
        return self.temperature * 9/5 + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9

    def display(self):
        print(f"{self.temperature}°C to Fahrenheit: {self.celsius_to_fahrenheit()}°F")
        print(f"{self.temperature}°F to Celsius: {self.fahrenheit_to_celsius()}°C")


p1 = TemperatureConverter(21)  
print("Using Celsius as input:")
p1.display()

p2 = TemperatureConverter(69)  
print("\nUsing Fahrenheit as input:")
p2.display()
