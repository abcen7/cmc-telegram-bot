from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, ParseMode

from handlers.constants import UserSearchMessages, EmployeeCreateMessages, SearchType
from handlers.fill_employee_handler import FillEmployee
from handlers.utils import get_result_or_failed, get_employee_card
from keyboards.constants import EMPLOYEE_SEARCH_DATA, EmployeeSearchButtons
from keyboards.executor import executor_cb, get_search_keyboard, get_main_keyboard, get_employee_card_actions_keyboard
from main import bot, dp
from services import EmployeesService


class SearchEmployee(StatesGroup):
    search_name_data = State()
    search_surname_data = State()
    search_job_title_data = State()
    search_project_data = State()


@dp.callback_query_handler(executor_cb.filter(action=EMPLOYEE_SEARCH_DATA))
async def process_search_employee_callback(call: CallbackQuery, callback_data) -> None:
    await bot.send_message(
        call.from_user.id,
        UserSearchMessages.LIST_SEARCH_COMMANDS.value,
        reply_markup=get_search_keyboard()
    )


@dp.message_handler(commands=["employee_search"])
async def process_search_employee_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        UserSearchMessages.LIST_SEARCH_COMMANDS.value
    )


@dp.callback_query_handler(executor_cb.filter(action=EmployeeSearchButtons.NAME_DATA.value))
async def process_search_employee_name_callback(call: CallbackQuery, callback_data) -> None:
    await bot.send_message(
        call.from_user.id,
        UserSearchMessages.USER_SEARCH_ASK.value,
        reply_markup=get_main_keyboard()
    )
    await SearchEmployee.search_name_data.set()


@dp.message_handler(commands=["search_employee_name"])
async def search_employee_by_name(message: types.Message) -> None:
    """
    Поиск по имени сотрудника
    """
    await message.answer(
        UserSearchMessages.USER_SEARCH_ASK.value,
        reply_markup=get_main_keyboard()
    )
    await SearchEmployee.search_name_data.set()


@dp.message_handler(state=SearchEmployee.search_name_data)
async def process_search_employee_by_name(message: types.Message, state: FSMContext):
    search_data = message.text
    api_result = await EmployeesService.search(search_data, SearchType.NAME)
    await get_result_or_failed(api_result, message)
    await state.finish()


@dp.message_handler(commands=["search_employee_surname"])
async def search_employee_by_surname(message: types.Message) -> None:
    """
    Поиск по фамилии сотрудника
    """
    await message.answer(
        UserSearchMessages.USER_SEARCH_ASK.value,
        reply_markup=get_main_keyboard()
    )
    await SearchEmployee.search_surname_data.set()


@dp.callback_query_handler(executor_cb.filter(action=EmployeeSearchButtons.SURNAME_DATA.value))
async def process_search_employee_surname_callback(call: CallbackQuery, callback_data) -> None:
    await bot.send_message(
        call.from_user.id,
        UserSearchMessages.USER_SEARCH_ASK.value,
        reply_markup=get_main_keyboard()
    )
    await SearchEmployee.search_surname_data.set()


@dp.message_handler(state=SearchEmployee.search_surname_data)
async def process_search_employee_by_surname(message: types.Message, state: FSMContext):
    search_data = message.text
    api_result = await EmployeesService.search(search_data, SearchType.SURNAME)
    await get_result_or_failed(api_result, message)
    await state.finish()


@dp.message_handler(commands=["search_employee_job_title"])
async def search_employee_by_job_title(message: types.Message) -> None:
    """
    Поиск по должности сотрудника
    """
    await message.answer(
        UserSearchMessages.USER_SEARCH_ASK.value,
        reply_markup=get_main_keyboard()
    )
    await SearchEmployee.search_job_title_data.set()


@dp.callback_query_handler(executor_cb.filter(action=EmployeeSearchButtons.JOB_TITLE_DATA.value))
async def process_search_employee_surname_callback(call: CallbackQuery, callback_data) -> None:
    await bot.send_message(
        call.from_user.id,
        UserSearchMessages.USER_SEARCH_ASK.value,
        reply_markup=get_main_keyboard()
    )
    await SearchEmployee.search_job_title_data.set()


@dp.message_handler(state=SearchEmployee.search_job_title_data)
async def process_search_employee_by_job_title(message: types.Message, state: FSMContext):
    search_data = message.text
    api_result = await EmployeesService.search(search_data, SearchType.JOB_TITLE)
    await get_result_or_failed(api_result, message)
    await state.finish()


@dp.message_handler(commands=["search_employee_project"])
async def search_employee_by_project(message: types.Message) -> None:
    """
    Поиск по проекту сотрудника
    """
    await message.answer(
        UserSearchMessages.USER_SEARCH_ASK.value,
        reply_markup=get_main_keyboard()
    )
    await SearchEmployee.search_project_data.set()


@dp.callback_query_handler(executor_cb.filter(action=EmployeeSearchButtons.PROJECT_DATA.value))
async def process_search_employee_surname_callback(call: CallbackQuery, callback_data) -> None:
    await bot.send_message(
        call.from_user.id,
        UserSearchMessages.USER_SEARCH_ASK.value,
        reply_markup=get_main_keyboard()
    )
    await SearchEmployee.search_project_data.set()


@dp.message_handler(state=SearchEmployee.search_project_data)
async def process_search_employee_by_project(message: types.Message, state: FSMContext):
    search_data = message.text
    api_result = await EmployeesService.search(search_data, SearchType.PROJECT)
    await get_result_or_failed(api_result, message)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data.startswith('employee_info_'))
async def process_view_employee_card(callback_data: CallbackQuery, call: CallbackQuery = None) -> None:
    employee_id = callback_data.data.replace('employee_info_', '')
    employee_from_api = await EmployeesService.get_one(employee_id)
    await bot.send_message(
        chat_id=callback_data.from_user.id,
        text=await get_employee_card(employee_from_api),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=False,
        reply_markup=get_employee_card_actions_keyboard(employee_id)
    )
