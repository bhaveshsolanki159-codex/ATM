class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "" 
        self.create_pin()

        self.menu()

    def create_pin(self):
            self.pin = int(input("Enter your new PIN: "))
            print("PIN created successfully!")

    def menu(self):
        print("Welcome to the ATM")
        user_input = input('''1. Deposit \n2. Withdraw \n3. Check Balance \n4. Exit \nEnter your choice: ''')

        if user_input == "1":
            self.deposit()
        elif user_input == "2":
            self.withdraw()
        elif user_input == "3": 
            self.check_balance()
        else:
            print("Goodbye!")
            exit()
    
    def deposit(self):
        temp = int(input("Enter the PIN: "))
        if temp == self.pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Invalid PIN!")
        self.menu()
    
    def withdraw(self):
        temp = int(input("Enter the PIN: "))
        if temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > self.balance:
                print("Insufficient funds!")
            else:
                self.balance -= amount
                print("Withdrawal successful!")
        else:
            print("Invalid PIN!")
        self.menu()

    def check_balance(self):
        print(f"Your balance is: {self.balance}")
        self.menu()

atm = ATM()



