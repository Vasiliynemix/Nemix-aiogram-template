from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.bot.structures.role import Role
from src.db.database import Database


class ModeratorFilter(BaseFilter):
    async def __call__(self, message: Message, db: Database):
        user = await db.user.get_by_user_id(user_id=message.from_user.id)
        if user.role == Role.MODERATOR or user.role == Role.ADMINISTRATOR:
            return True
