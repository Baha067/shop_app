from psycopg2 import errors
import repository
from db import get_connection

conn = get_connection()
try:
    order_id = repository.place_order(conn, 1, [(1, 2), (3, 1)])
    conn.commit()
    print("Saved order", order_id)
except errors.CheckViolation as error:
    conn.rollback()
    print("Order cancelled: not enough stock", error.diag.constraint_name)
except ValueError as error:
    conn.rollback()
    print("Order cancelled:", error)
finally:
    conn.close()

