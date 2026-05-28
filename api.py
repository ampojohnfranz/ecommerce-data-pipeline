from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class NewOrder(BaseModel):
    order_id: str
    date: str
    customer: str
    sku: str
    category: str
    quantity: int
    unit_price: float
    status: str


@app.get("/v2/orders")
def get_all_orders():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    conn.close()

    formatted_orders = []
    for row in rows:
        formatted_orders.append({
            "order_id": row[0],
            "date": row[1],
            "customer": row[2],
            "sku": row[3],
            "category": row[4],
            "quantity": row[5],
            "unit_price": row[6],
            "status": row[7]
        })

    return {"inventory_status": formatted_orders}


@app.post("/orders")
def add_new_order(order: NewOrder):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO orders 
        (order_id, date, customer, sku, category, quantity, unit_price, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (order.order_id, order.date, order.customer, order.sku, order.category, order.quantity, order.unit_price,
          order.status))

    conn.commit()
    conn.close()

    return {"message": f"Order {order.order_id} for {order.customer} added."}


@app.put("/orders/{order_id}/status")
def update_order_status(order_id: str, new_status: str):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE orders SET status = ? WHERE order_id = ?
    ''', (new_status, order_id))

    conn.commit()
    rows_changed = cursor.rowcount
    conn.close()

    if rows_changed == 0:
        return {"error": f"Order {order_id} not found."}

    return {"message": f"Order {order_id} status updated to {new_status}."}


@app.delete("/orders/{order_id}")
def delete_order(order_id: str):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))

    conn.commit()
    rows_changed = cursor.rowcount
    conn.close()

    if rows_changed == 0:
        return {"error": f"Order {order_id} not found."}

    return {"message": f"Order {order_id} successfully deleted."}