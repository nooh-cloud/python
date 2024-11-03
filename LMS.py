
class Book:
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        self.available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully.")

    def checkout_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn and b.available), None)
        
        if member and book:
            book.available = False
            member.borrowed_books.append(book)
            print(f"Book '{book.title}' checked out to {member.name}.")
        else:
            print("Checkout failed. Book may be unavailable or member ID may be invalid.")

    def display_member_details(self, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member:
            print(f"Member Name: {member.name}")
            print("Borrowed Books:")
            for book in member.borrowed_books:
                print(f"  - {book.title} by {book.author}")
        else:
            print("Member not found.")

    def menu(self):
        while True:
            print("\nLibrary Management Menu")
            print("1. Add a new book")
            print("2. Register a new member")
            print("3. Checkout a book")
            print("4. Display member details")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter author: ")
                self.add_book(Book(title, author,))
            elif choice == '2':
                name = input("Enter member name: ")
                member_id = input("Enter member ID: ")
                self.register_member(Member(name, member_id))
            elif choice == '3':
                member_id = input("Enter member ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                self.checkout_book(member_id, isbn)
            elif choice == '4':
                member_id = input("Enter member ID: ")
                self.display_member_details(member_id)
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

library = Library()
library.menu()
