import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.bot.structures.role import Role
from src.db.models import Base


class User(Base):
    user_id: Mapped[int] = mapped_column(sa.BigInteger, unique=True, nullable=False)
    user_name: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=True)

    first_name: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=True)
    second_name: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=True)

    language_code: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=True)
    is_premium: Mapped[bool] = mapped_column(sa.Boolean, unique=False, nullable=False)

    role: Mapped[Role] = mapped_column(sa.Enum(Role), default=Role.USER)
