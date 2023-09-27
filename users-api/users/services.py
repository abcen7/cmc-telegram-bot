from .exceptions import UserIsAlreadyExist
from .models import User
from .repositories import UsersRepository


class UsersService:
    object_model = User

    def __init__(self) -> None:
        self.repository = UsersRepository()

    async def create(self, create_object: object_model) -> object_model:
        if await self.repository.is_user_exist(create_object.telegram_id):
            raise UserIsAlreadyExist
        return await self.repository.create(dict(create_object))
