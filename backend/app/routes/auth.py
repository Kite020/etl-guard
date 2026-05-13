from fastapi import APIRouter

from pydantic import BaseModel

from app.database import SessionLocal

from app.models.user_model import User

from app.auth.hash_password import (
    hash_password,
    verify_password
)

from app.auth.auth_handler import (
    create_access_token
)

router = APIRouter()


class SignupModel(BaseModel):

    username: str

    email: str

    password: str


class LoginModel(BaseModel):

    email: str

    password: str


@router.post("/signup")
def signup(user: SignupModel):

    db = SessionLocal()

    hashed_password = hash_password(
        user.password
    )

    new_user = User(

        username=user.username,

        email=user.email,

        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.close()

    return {
        "message": "User created successfully"
    }


@router.post("/login")
def login(user: LoginModel):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:

        return {
            "error": "Invalid email"
        }

    valid_password = verify_password(

        user.password,

        existing_user.password
    )

    if not valid_password:

        return {
            "error": "Invalid password"
        }

    token = create_access_token({

        "sub": existing_user.email
    })

    return {

        "access_token": token,

        "token_type": "bearer"
    }