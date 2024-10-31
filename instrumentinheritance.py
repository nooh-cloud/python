class Instrument:
    def play(self):
        return "Playing instrument"
    
class Guitar(Instrument):
    def strum(self):
        return "Strumming the guitar"
    
guitar = Guitar()

print(guitar.play())
print(guitar.strum())