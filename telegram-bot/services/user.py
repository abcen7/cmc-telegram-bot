from aiogram.dispatcher import FSMContext
from aiohttp import ClientSession, ClientError

from config import API_URL


class UserService:
    @staticmethod
    async def new(state: FSMContext):
        data = await state.get_data()

        async with ClientSession() as session:
            try:
                async with session.post(API_URL, json=data) as response:
                    response.raise_for_status()
            except ClientError as err:
                print(f"An error occurred: {err}")
