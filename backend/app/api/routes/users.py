from fastapi import APIRouter
from sqlmodel import select

from app.crud import users
from app.api.dependancies import SessionDep
from app.models.users import User, UserCreate

router = APIRouter()

@router.get("/users", response_model=list[User])
async def get_users(session: SessionDep):
    result = await session.exec(select(User))
    users = result.all()
    return [User(id=user.id, username=user.username, email=user.email) for user in users]


@router.post("/users", response_model=User)
async def create_user(user_in: UserCreate, session: SessionDep):
    user = await users.create_user(session=session, user_in=user_in)
    return user