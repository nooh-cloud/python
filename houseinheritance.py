class Building:
    def gh(self):
        return "Basic Structure"

class House(Building):
    def hj(self):
        return "Living in the house"
    
house = House()

print(house.gh())
print(house.hj())