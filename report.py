import repository 
from db import get_connection

conn = get_connection()
try:
    for name, size, pairs_sold, revenue in repository.get_sales_report(conn):
        print(f"{name} ({size}): {pairs_sold} pairs, {revenue}")
finally:
    conn.close()
    