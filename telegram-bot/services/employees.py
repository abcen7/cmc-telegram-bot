from typing import List, Dict, NoReturn

from aiogram.dispatcher import FSMContext
from aiohttp import ClientSession, ClientError

from config import API_URL
from keyboards.constants import OPTIONAL_FIELD


class EmployeesService:
    API_EMPLOYEES = API_URL + '/employees'

    @staticmethod
    def _prepare_data(data: Dict[str, str]) -> Dict[str, str]:
        prepared_data = {}
        for key in data:
            if data[key] != OPTIONAL_FIELD:
                prepared_data[key] = data[key]
        return prepared_data

    @staticmethod
    async def new(state: FSMContext) -> NoReturn:
        data = await state.get_data()
        prepared_data = EmployeesService._prepare_data(data)
        print(prepared_data)
        async with ClientSession() as session:
            try:
                async with session.post(EmployeesService.API_EMPLOYEES, json=prepared_data) as response:
                    response.raise_for_status()
            except ClientError as err:
                print(f"An error occurred: {err}")
