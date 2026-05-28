import json
import sqlite3

with open('orders.json', 'r') as file:
    raw_data = json.load(file)

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        date TEXT,
        customer TEXT,
        sku TEXT,
        category TEXT,
        quantity INTEGER,
        unit_price REAL,
        status TEXT
    )
''')

for order in raw_data:
    cursor.execute('''
        INSERT OR IGNORE INTO orders 
        (order_id, date, customer, sku, category, quantity, unit_price, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order['order_id'],
        order['date'],
        order['customer'],
        order['sku'],
        order['category'],
        order['quantity'],
        order['unit_price'],
        order['status']
    ))

    print(f"Logged {order['order_id']} for {order['customer']}.")

conn.commit()
conn.close()
print("Database successfully built.")