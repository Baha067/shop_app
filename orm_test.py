from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from config import DB_SETTINGS
from models import Product

url = (
    f"postgresql+psycopg2://{DB_SETTINGS['user']}:{DB_SETTINGS['password']}"
    f"@{DB_SETTINGS['host']}:{DB_SETTINGS['port']}/{DB_SETTINGS['dbname']}"
)
engine = create_engine(url)

with Session(engine) as session:
    for product in session.scalars(select(Product).order_by(Product.id)):
        print(product.id, product.name, product.size, product.stock)

with Session(engine) as session:
    product = session.get(Product, 3)
    print("Before:", product.stock)
    product.stock = product.stock - 10
    try:
        session.commit()
    except Exception as error:
        session.rollback()
        print("Cancelled:", type(error).__name__)
    print("After:", product.stock)
    