from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://cn_user:lkpeelmlhAbVZ2L6VMBteKCosPDZcLDH@dpg-d8imosl8nd3s73dovc4g-a/cn"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

try:
    with engine.connect() as conn:
        print("✅ DB Connected Successfully")
except Exception as e:
    print("❌ DB Connection Failed:", e)