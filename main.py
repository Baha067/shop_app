import repository
from db import get_connection

conn = get_connection()
try:
    order_id = repository.place_order(conn, 1, [(1, 2), (3, 1)])
    conn.commit()
    print("Saved order", order_id)
except ValueError as error:
    conn.rollback()
    print("Order cancelled:", error)
    conn.commit()
finally:
    conn.close()

