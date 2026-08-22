import sqlite3

DATABASE = "atm.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            pin TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            balance REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def create_user(name, pin, balance=10000):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, pin, balance) VALUES (?, ?, ?)",
        (name, pin, balance)
    )

    conn.commit()
    conn.close()


def login(pin):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, balance FROM users WHERE pin = ?",
        (pin,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def update_balance(user_id, balance):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET balance = ? WHERE id = ?",
        (balance, user_id)
    )

    conn.commit()
    conn.close()


def add_transaction(user_id, transaction_type, amount, balance):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (user_id, type, amount, balance)
        VALUES (?, ?, ?, ?)
    """, (user_id, transaction_type, amount, balance))

    conn.commit()
    conn.close()


def get_transactions(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT type, amount, balance, timestamp
        FROM transactions
        WHERE user_id = ?
        ORDER BY id DESC
    """, (user_id,))

    transactions = cursor.fetchall()

    conn.close()

    return transactions
