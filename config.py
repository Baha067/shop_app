import os
from dotenv import load_dotenv

load_dotenv()

DB_SETTINGS = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

missing = [key for key, value in DB_SETTINGS.items() if not value]
if missing:
    raise RuntimeError(f"Missing settings in .env: {', '.join(missing)}")
