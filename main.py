import random  # Required to generate account numbers

# 🔹 Step 1: Define the function FIRST
def create_account():
    name = input("Enter your name: ")
    password = input("Create a password: ")
    try:
        balance = float(input("Enter your initial deposit: "))
    except ValueError:
        print("Invalid amount! Try again.")
        return

    account_number = random.randint(100000, 999999)

    with open("accounts.txt", "a") as file:
        file.write(f"{account_number},{name},{password},{balance}\n")

    print(f"\nAccount created successfully!")
    print(f"Your account number is: {account_number}")
    print("Please save it for login.\n")


def login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    found = False
    updated_lines = []

    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                if len(data) == 4:
                    acc_no, name, passw, balance = data
                    if acc_no == account_number and passw == password:
                        found = True
                        print(f"\nLogin successful! Welcome back, {name}.")
                        print(f"Your current balance is: ₹{balance}")
                        
                        # After login, show sub-menu
                        while True:
                            print("\n1. Deposit")
                            print("2. Withdraw")
                            print("3. View Transactions History")
                            print("4. Logout")
                            sub_choice = input("Choose an option: ")

                            if sub_choice == '1':
                                amount = float(input("Enter amount to deposit: "))
                                balance = float(balance) + amount
                                print(f"Deposit successful! New balance: ₹{balance}")
                                with open("transactions.txt", "a") as tf:
                                    from datetime import date
                                    tf.write(f"{account_number},Deposit,{amount},{date.today()}\n")
                            elif sub_choice == '2':
                                amount = float(input("Enter amount to withdraw: "))
                                if float(balance) >= amount:
                                    balance = float(balance) - amount
                                    print(f"Withdrawal successful! New balance: ₹{balance}")
                                    with open("transactions.txt", "a") as tf:
                                        from datetime import date
                                        tf.write(f"{account_number},Withdrawal,{amount},{date.today()}\n")
                                else:
                                    print("Insufficient balance!")
                            elif sub_choice == '3':
                               print("\n--- Transaction History ---")
                               try:
                                   with open("transactions.txt", "r") as tf:
                                        found_txn = False
                                        for line in tf:
                                            txn_data = line.strip().split(",")
                                            if txn_data[0] == account_number:
                                              print(f"{txn_data[3]} - {txn_data[1]} of ₹{txn_data[2]}")
                                              found_txn = True
                                        if not found_txn:
                                          print("No transactions found.")
                               except FileNotFoundError:
                                    print("No transaction file found.")        
                            elif sub_choice == '4':
                                print("Logged out successfully.")
                                break
                            else:
                                print("Invalid choice. Try again.")

                        # Update account balance in file
                        updated_line = f"{acc_no},{name},{passw},{balance}\n"
                        updated_lines.append(updated_line)
                    else:
                        updated_lines.append(line)
        if found:
            with open("accounts.txt", "w") as file:
                file.writelines(updated_lines)
        else:
            print("Invalid account number or password. Please try again.")

    except FileNotFoundError:
        print("Accounts file not found. Please create an account first.")
        
def view_transactions():
    username = input("Enter your username to view transactions: ")

    try:
        with open("transactions.txt", "r") as file:
            transactions = file.readlines()

        user_transactions = [t.strip() for t in transactions if t.startswith(username)]

        if user_transactions:
            print("\n--- Transaction History ---")
            for t in user_transactions:
                print(t)
        else:
            print("No transactions found for this user.")

    except FileNotFoundError:
        print("Transaction file not found.")
# 🔹 Step 2: Now write the menu function
def main_menu():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. View Transaction History")
        print("4. Logged out successfully.")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()  # Now Python knows this function
        elif choice == '2':
            login()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            print("Logged out succesfully.")
            break
        else:
            print("Invalid choice. Try again.")

# 🔹 Step 3: Start the program by calling main_menu
main_menu()