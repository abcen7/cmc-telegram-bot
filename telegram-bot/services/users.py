from typing import NoReturn

from aiohttp import \
    ClientSession, \
    ClientError, \
    TCPConnector

from config import API_URL


class UsersService:
    API_USERS = API_URL + '/users'

    @staticmethod
    async def new(user_id: int) -> NoReturn:
        async with ClientSession(connector=TCPConnector(verify_ssl=False)) as session:
            try:
                async with session.post(UsersService.API_USERS, json={
                    "telegram_id": user_id
                }) as response:
                    response.raise_for_status()
            except ClientError as err:
                print(f"User is already exists... {err}")
