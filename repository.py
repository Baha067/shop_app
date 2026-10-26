def add_item(conn, order_id, product_id, quantity):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO order_items (order_id, product_id, quantity, unit_price) "
            "SELECT %s, p.id, %s, p.price FROM products p WHERE p.id = %s;",
            (order_id, quantity, product_id),
        )
        if cur.rowcount == 0:
            raise ValueError(f"Product {product_id} does not exist")
def place_order(conn, customer_id, items):
    order_id = create_order(conn, customer_id)
    for product_id, quantity in items:
        add_item(conn, order_id, product_id, quantity)
    return order_id

def create_order(conn, customer_id):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO orders (customer_id) VALUES (%s) RETURNING id;",
            (customer_id,),
        )
        return cur.fetchone()[0]
        