from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, Base
from models import User
from schemas import UserRegister, UserLogin

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "https://cn-project-phi.vercel.app/", 
    "http://localhost:5173",            # local development
    "https://cn-project-phi.vercel.app/signup",      # Vercel frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "WELCOME TO CN-PROJECT-BACKEND! welcome ssrgsp"}


# Register API
@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "success": True,
        "message": "User registered successfully",
        "user_id": new_user.id
    }


# Login API
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email"
        )

    if db_user.password != user.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    return {
        "success": True,
        "message": "Login successful",
        "username": db_user.username
    }


# Get All Users
@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        for user in users
    ]