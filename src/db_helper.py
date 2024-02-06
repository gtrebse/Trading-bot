import sqlite3
import time

# Initialize the database and create a table for the given ticker
def init_db(ticker):
    db_name = f'./data/arbitrage_opportunities.db'
    table_name = f'pair_{ticker}'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            ticker TEXT,
            action1 TEXT,
            action2 TEXT,
            ask REAL,
            bid REAL,
            ratio REAL,
            profit REAL,
            timestamp REAL
        )
    ''')
    connection.commit()
    connection.close()

# Function to log a trade to the SQLite database for the given ticker
def log_trade(ticker, action1, action2, ask, bid, ratio, profit):
    db_name = f'./data/arbitrage_opportunities.db'
    table_name = f'pair_{ticker}'
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(f'''
        INSERT INTO {table_name} (ticker, action1, action2, ask, bid, ratio, profit, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ticker, action1, action2, ask, bid, ratio, profit, time.time()))
    connection.commit()
    connection.close()