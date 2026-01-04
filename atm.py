correct_pin = "1028"
balance = 50000
account_name = "Ovedje Godbless"
account_number = "2360922190"
bank_name = "Polar Bank"

attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print(f"\n===== WELCOME TO {bank_name} ATM =====")
        print("Account Name:", account_name)
        print("Account Number:", account_number)
        print("--------------------------------------")

        while True:  # Menu loop
            print("\nMenu:")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                print("\nYour balance is ₦", balance)

            elif choice == "2":
                print("\n--- Withdrawal ---")
                acc_num = input("Enter account number: ")

                if acc_num == account_number:
                    while True:  # Withdraw validation loop
                        amount = int(input("Enter amount to withdraw: ₦"))

                        if amount > balance:
                            print(f"❌ Insufficient balance. Your balance is ₦{balance}.")
                            print("Please enter an amount within your balance.")
                        else:
                            confirm = input(
                                f"Confirm withdrawal of ₦{amount} from {account_name}? (yes/no): "
                            )
                            if confirm.lower() == "yes":
                                balance -= amount
                                print("✅ Withdrawal successful")
                                print("Remaining balance: ₦", balance)
                                break  # Exit withdraw loop
                            else:
                                print("Transaction cancelled")
                                break  # Exit withdraw loop
                else:
                    print("❌ Account number mismatch")

            elif choice == "3":
                print("\n--- Deposit ---")
                amount = int(input("Enter amount to deposit: ₦"))
                balance += amount
                print("✅ Deposit successful")
                print("New balance: ₦", balance)
                continue  # Loop back to menu cleanly

            elif choice == "4":
                print("Thank you for using Polar Bank ATM. Goodbye!")
                break  # Exit menu loop

            else:
                print("❌ Invalid option. Please choose 1-4.")

        break  # Exit PIN check loop after successful login

    else:
        attempts -= 1
        print("❌ Wrong PIN")
        print("Attempts left:", attempts)

        if attempts == 0:
            print("Card blocked. Too many wrong attempts.")





