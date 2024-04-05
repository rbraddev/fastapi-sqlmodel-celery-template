from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.users import User, UserCreate


async def create_user(*, session: AsyncSession, user_in: UserCreate) -> User:
    user = User.model_validate(user_in)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user