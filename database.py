import sqlite3

DATABASE = "atm.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS account (
            id INTEGER PRIMARY KEY,
            balance REAL NOT NULL,
            pin TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            balance REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM account")

    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO account (balance, pin) VALUES (?, ?)",
            (10000, "1234")
        )

    conn.commit()
    conn.close()


def get_account():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance, pin FROM account WHERE id = 1"
    )

    account = cursor.fetchone()

    conn.close()

    return account


def update_balance(balance):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE account SET balance = ? WHERE id = 1",
        (balance,)
    )

    conn.commit()
    conn.close()


def add_transaction(transaction_type, amount, balance):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (type, amount, balance)
        VALUES (?, ?, ?)
    """, (transaction_type, amount, balance))

    conn.commit()
    conn.close()


def get_transactions():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT type, amount, balance, timestamp
        FROM transactions
        ORDER BY id DESC
    """)

    transactions = cursor.fetchall()

    conn.close()

    return transactions
