class BankAccount:
    def __init__(self, account_holder, user_id, password, initial_balance=0):
        self.account_holder = account_holder
        self.user_id = user_id
        self.password = password
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: {self.balance}")


# Dictionary to store all accounts
accounts = {}


def create_account():
    print("Create a new account:")
    account_holder = input("Enter your full name: ")
    user_id = input("Choose a user ID: ")
    password = input("Choose a password: ")

    if user_id in accounts:
        print("User ID already exists. Please choose a different one.")
        return

    accounts[user_id] = BankAccount(account_holder, user_id, password)
    print("Account created successfully!")


def login():
    print("Login to your account:")
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")

    if user_id in accounts and accounts[user_id].password == password:
        print("Login successful!")
        return accounts[user_id]
    else:
        print("Invalid user ID or password.")
        return None


def main():
    print("Welcome to the Banking System!")

    while True:
        print("Please choose an option:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            account = login()
            if account:
                while True:
                    print("Please choose an option:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    option = input("Enter your choice (1/2/3/4): ")

                    if option == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                    elif option == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                    elif option == '3':
                        account.check_balance()
                    elif option == '4':
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()