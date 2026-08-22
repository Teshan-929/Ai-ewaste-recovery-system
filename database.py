import sqlite3

connection = sqlite3.connect("ewaste.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    market_value REAL NOT NULL,
    extraction_cost REAL NOT NULL,
    shipping_cost REAL NOT NULL
)
""")

connection.commit()

print("Components table created successfully!")

connection.close()