from sqlalchemy import create_engine 
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from config import DB_SETTINGS 
import orm_repository

url = (
    f"postgresql+psycopg2://{DB_SETTINGS['user']}:{DB_SETTINGS['password']}"
    f"@{DB_SETTINGS['host']}:{DB_SETTINGS['port']}/{DB_SETTINGS['dbname']}"
)
engine = create_engine(url)

with Session(engine) as session:
    try:
        order_id = orm_repository.place_order(session, 1, [(1, 2), (3, 1)])
        session.commit()
        print("Saved order", order_id)
    except ValueError as error:
        session.rollback()
        print("Order cancelled:", error)
    except IntegrityError:
        session.rollback()
        print("Order cancelled: not enough stock")
        