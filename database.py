from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Database Connection Test
try:
    with engine.connect() as connection:
        print("✅ PostgreSQL Database Connected Successfully!")
except Exception as e:
    print("❌ Database Connection Failed!")
    print("Error:", e)