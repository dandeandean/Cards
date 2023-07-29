from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, create_engine


class CardCategoryLink(SQLModel, table=True):
    card_id: Optional[int] = Field(
        default=None, foreign_key="card.id", primary_key=True
    )
    category_id: Optional[int] = Field(
        default=None, foreign_key="category.id", primary_key=True
    )


class Card(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    front: str
    back: str

    categories: List["Category"] = Relationship(
        back_populates="cards", link_model=CardCategoryLink
    )


class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    cards: List["Card"] = Relationship(
        back_populates="categories", link_model=CardCategoryLink
    )


class PracticeType(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str


def right_now() -> str:
    return datetime.now().isoformat()


class PracticeSession(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    practice_id: int = Field(foreign_key="practicetype.id")
    start_datetime: str = Field(default_factory=right_now)
    end_datetime: Optional[str] = None

    def update_end_datetime(self):
        self.end_datetime = datetime.now().isoformat()


class PracticeHistory(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    card_id: int = Field(foreign_key="card.id")
    session_id: int = Field(foreign_key="practicesession.id")
    datetime: str = Field(default_factory=right_now)
    correct: bool


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


def get_engine(name: str = "database.db", echo: bool = False):
    sqlite_file_name = name
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, echo=echo, connect_args=connect_args)

    create_db_and_tables(engine)

    return engine
