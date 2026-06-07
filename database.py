from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔥 Direct Render PostgreSQL URL yaha paste karo
DATABASE_URL = "postgresql+psycopg2://cn_project_user:rama@dpg-d8iijncm0tmc73bljvkg-a.ohio-postgres.render.com/cn_project"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Connection test
try:
    with engine.connect() as connection:
        print("✅ PostgreSQL Connected Successfully!")
except Exception as e:
    print("❌ Connection Failed:", e)