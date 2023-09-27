import datetime
import uuid
from typing import Dict, List, NoReturn

from aiogram import types
from aiogram.types import ParseMode

import config
from handlers.constants import \
    SearchResultMessages, \
    API_TO_RESULT, \
    NEW_LINE, \
    AVATAR_PATH, \
    CREATED, \
    ID, \
    EmployeeSearchMessages
from keyboards.executor import get_employees_list_keyboard
from services import EmployeesService


# TODO: refactor to class builder
async def get_employee_card(employee: Dict[str, str]) -> str:
    employee_card = []
    for key in employee:
        if key == ID:
            employee_card.append(f'<b>ID: </b><pre>{employee[key]}</pre>')
        if key == AVATAR_PATH and employee[key] is not None:
            avatar_file = await EmployeesService.get_file(employee[key])
            if config.LOCAL_DEVELOPMENT:
                avatar_file = avatar_file.replace('host.docker.internal', 'localhost')
            employee_card.append(f'<a href="{avatar_file}">&#8205;</a>')
        if key == CREATED:
            employee_card.append(f'<b>Дата прихода</b>: {datetime.datetime.fromtimestamp(employee[key])}')
        if key in API_TO_RESULT and employee[key] is not None:
            employee_card.append(str(API_TO_RESULT[key]) + str(employee[key]))
    return NEW_LINE.join(employee_card)


async def get_result_or_failed(
        employees: List[Dict[str, str]],
        message: types.Message,
) -> NoReturn:
    if not employees or len(employees) == 0:
        await message.answer(
            SearchResultMessages.SEARCH_RESULT_NOT_FOUND.value,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=False
        )
    else:
        await message.answer(
            EmployeeSearchMessages.LIST_EMPLOYEES.value,
            reply_markup=await get_employees_list_keyboard(employees)
        )


async def generate_unique_filename() -> str:
    return f'{str(uuid.uuid4())}.jpg'
