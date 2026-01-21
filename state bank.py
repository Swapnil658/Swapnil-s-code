balance = 10000
correct_pin = 1234
attempts = 0

# PIN verification (max 3 attempts)
while attempts < 3:
    pin = int(input("Enter your 4-digit PIN: "))
    if pin == correct_pin:
        print("PIN verified successfully\n")
        break
    else:
        print("Incorrect PIN\n")
        attempts += 1

if attempts == 3:
    print("Too many wrong attempts. Card blocked.")
else:
    while True:
        print("----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is: ₹", balance)

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Deposit successful")
                print("Updated balance: ₹", balance)
            else:
                print("Invalid amount")

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                print("Withdrawal successful")
                print("Remaining balance: ₹", balance)

        elif choice == 4:
            print("Thank you for using ATM 😊")
            break

        else:
            print("Invalid choice. Try again.")
