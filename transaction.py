import json
from datetime import datetime

DATA_FILE = "data.json"


def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_transaction(transaction_type, amount, balance):
    data = load_data()

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance": balance,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data["transactions"].append(transaction)
    save_data(data)


def show_transactions():
    data = load_data()

    if not data["transactions"]:
        print("\nNo transactions found.")
        return

    print("\n========== TRANSACTION HISTORY ==========")

    for i, transaction in enumerate(data["transactions"], start=1):
        print(f"\nTransaction {i}")
        print(f"Type     : {transaction['type']}")
        print(f"Amount   : ₹{transaction['amount']:.2f}")
        print(f"Balance  : ₹{transaction['balance']:.2f}")
        print(f"Date/Time: {transaction['time']}")

    print("\n=========================================")
