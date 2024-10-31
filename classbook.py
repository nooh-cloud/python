class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True
        
    def borrow(self):
        if self.available:
            self.available = False
            print("The book is has borrowed.")
        else :
            print("The book is currently unavailable.")
            
    def return_book(self):
        self.available = True
        print("The book is available")
        
    def display(self):
        availability = "Available" if self.available else "unavailable"
        print(f"Title: {self.title}, Author: {self.author}, Status: {availability}")
        
p1 = book('hello','mark')
 
p1.display()
p1.borrow()