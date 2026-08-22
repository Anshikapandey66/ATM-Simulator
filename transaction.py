from datetime import datetime

transactions = []


def add_transaction(transaction_type, amount, balance):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance": balance,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    transactions.append(transaction)


def show_transactions():
    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n========== TRANSACTION HISTORY ==========")

    for i, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction {i}")
        print(f"Type     : {transaction['type']}")
        print(f"Amount   : ₹{transaction['amount']:.2f}")
        print(f"Balance  : ₹{transaction['balance']:.2f}")
        print(f"Date/Time: {transaction['time']}")

    print("\n=========================================")
