import sqlite3

connection = sqlite3.connect("ewaste.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer TEXT NOT NULL,
    part_number TEXT NOT NULL,
    component_type TEXT NOT NULL,
    reference_price REAL,
    currency TEXT DEFAULT 'USD',
    price_source TEXT,
    last_updated TEXT,
    extraction_cost REAL DEFAULT 0,
    testing_cost REAL DEFAULT 0,
    shipping_cost REAL DEFAULT 0
)
""")

connection.commit()

print("Components table created successfully!")

connection.close()