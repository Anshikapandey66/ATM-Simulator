balance = 10000
correct_pin = "1234"

print("=" * 35)
print("        PYTHON ATM SIMULATOR")
print("=" * 35)

# PIN Login
for attempt in range(3):
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("\n✅ Login successful!")
        break
    else:
        print("❌ Incorrect PIN.")

else:
    print("\n🚫 Too many incorrect attempts.")
    exit()


# ATM Menu
while True:
    print("\n" + "=" * 35)
    print("           ATM MENU")
    print("=" * 35)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # Check Balance
    if choice == "1":
        print(f"\n💰 Current Balance: ₹{balance:.2f}")

    # Deposit
    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: ₹"))

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
            else:
                balance += amount
                print(f"✅ ₹{amount:.2f} deposited successfully.")
                print(f"💰 New Balance: ₹{balance:.2f}")

        except ValueError:
            print("❌ Please enter a valid amount.")

    # Withdraw
    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
            elif amount > balance:
                print("❌ Insufficient balance.")
            else:
                balance -= amount
                print(f"✅ ₹{amount:.2f} withdrawn successfully.")
                print(f"💰 Remaining Balance: ₹{balance:.2f}")

        except ValueError:
            print("❌ Please enter a valid amount.")

    # Change PIN
    elif choice == "4":
        old_pin = input("Enter current PIN: ")

        if old_pin == correct_pin:
            new_pin = input("Enter new 4-digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                correct_pin = new_pin
                print("✅ PIN changed successfully.")
            else:
                print("❌ PIN must contain exactly 4 digits.")
        else:
            print("❌ Incorrect current PIN.")

    # Exit
    elif choice == "5":
        print("\nThank you for using Python ATM Simulator! 👋")
        break

    else:
        print("❌ Invalid choice. Please try again.")
