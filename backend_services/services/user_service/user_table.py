from datetime import datetime
from typing import Literal, Optional

from sqlalchemy import JSON, Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend_services.db.base_table import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str | None] = mapped_column(String(30))
    last_name: Mapped[str | None] = mapped_column(String(30))
    middle_name: Mapped[str | None] = mapped_column(String(30))
    birth_date: Mapped[str | None] = mapped_column(String)
    age: Mapped[int | None] = mapped_column(Integer)
    gender: Mapped[Literal["male", "female"] | None] = mapped_column(String)
    nationality: Mapped[str | None] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    contact: Mapped[Optional["Contact"]] = relationship(
        back_populates="user", cascade="all, delete-orphan", uselist=False
    )
    statistics: Mapped[Optional["Statistics"]] = relationship(
        back_populates="user", cascade="all, delete-orphan", uselist=False
    )


class Contact(Base):
    __tablename__ = "contact"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    # email: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)
    address: Mapped[dict] = mapped_column(JSON)
    networks: Mapped[list[dict]] = mapped_column(JSON)

    user: Mapped[User] = relationship(back_populates="contact", uselist=False)


class Statistics(Base):
    __tablename__ = "statistics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    registration_date: Mapped[datetime] = mapped_column(DateTime)
    last_login: Mapped[datetime] = mapped_column(DateTime)
    login_count: Mapped[int] = mapped_column(Integer)
    rating: Mapped[float] = mapped_column(Float)

    user: Mapped[User] = relationship(back_populates="statistics", uselist=False)
