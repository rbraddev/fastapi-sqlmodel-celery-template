from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username: str
    email: str

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)

class UserCreate(UserBase):
    pass

