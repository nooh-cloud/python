
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.account = None

    def create_account(self, account_number):
        self.account = Account(account_number)
        print(f"Account created for {self.name} with account number {account_number}.")

class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer '{customer.name}' added successfully.")

    def menu(self):
        while True:
            print("\nBanking Application Menu")
            print("1. Create an account")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. View account details")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                name = input("Enter customer name: ")
                customer_id = input("Enter customer ID: ")
                account_number = input("Enter new account number: ")
                customer = Customer(name, customer_id)
                customer.create_account(account_number)
                self.add_customer(customer)
            elif choice == '2':
                account_number = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                customer = next((c for c in self.customers if c.account and c.account.account_number == account_number), None)
                if customer:
                    customer.account.deposit(amount)
                else:
                    print("Account not found.")
            elif choice == '3':
                account_number = input("Enter account number: ")
                amount = float(input("Enter withdrawal amount: "))
                customer = next((c for c in self.customers if c.account and c.account.account_number == account_number), None)
                if customer:
                    customer.account.withdraw(amount)
                else:
                    print("Account not found.")
            elif choice == '4':
                account_number = input("Enter account number: ")
                customer = next((c for c in self.customers if c.account and c.account.account_number == account_number), None)
                if customer:
                    print(f"Account balance for {customer.name}: {customer.account.get_balance()}")
                else:
                    print("Account not found.")
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

bank = Bank()
bank.menu()
