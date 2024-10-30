class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
        
    def average(self):
        return sum(self.mark) / len(self.mark)
    
    def display(self):
        print(self.name)
        print(self.average())
        
p1 = student("nooh",[100,80,50,70])
p1.display()

        