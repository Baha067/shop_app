from models import Order, OrderItem, Product


def create_order(session, customer_id):
    order = Order(customer_id=customer_id)
    session.add(order)
    session.flush()
    return order.id
    
def add_item(session, order_id, product_id, quantity):
    product = session.get(Product, product_id)
    if product is None:
        raise ValueError(f"Product {product_id} does not exist")

    session.add(
        OrderItem(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity,
            unit_price=product.price,
        )
    )
    product.stock = product.stock - quantity

def place_order(session, customer_id, items):
    order_id = create_order(session, customer_id)
    for product_id, quantity in items:
        add_item(session, order_id, product_id, quantity)
    return order_id
    