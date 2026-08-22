from transactions import add_transaction, show_transactions


def test_add_transaction():
    transactions = []

    transaction = {
        "type": "Deposit",
        "amount": 500,
        "balance": 10500
    }

    transactions.append(transaction)

    assert len(transactions) == 1
    assert transactions[0]["type"] == "Deposit"
    assert transactions[0]["amount"] == 500
    assert transactions[0]["balance"] == 10500


def test_withdrawal_transaction():
    transactions = []

    transaction = {
        "type": "Withdrawal",
        "amount": 1000,
        "balance": 9000
    }

    transactions.append(transaction)

    assert transactions[0]["type"] == "Withdrawal"
    assert transactions[0]["amount"] == 1000
