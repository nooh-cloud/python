class Appliance:
    def on(self):
        return "Appliance is on"
    
class Washingmachine(Appliance):
    def work(self):
        return "Washing clothes"
    
washingmachine = Washingmachine()

print(washingmachine.on())
print(washingmachine.work())
