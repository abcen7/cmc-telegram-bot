import os.path
import uuid
from pathlib import Path

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

import services
from config import TEMP_STATIC_PATH
from handlers.constants import UserAddMessages
from handlers.default import process_commands_button
from keyboards.executor import executor_cb, get_optional_field_keyboard, get_stop_filling_keyboard, get_main_keyboard
from main import bot, dp

from keyboards.constants import \
    USER_ADD_DATA, \
    STOP_FILLING
from services import EmployeesService


class FillEmployee(StatesGroup):
    name = State()
    patronymic = State()
    surname = State()
    job_title = State()
    project = State()
    avatar_path = State()


@dp.callback_query_handler(executor_cb.filter(action=USER_ADD_DATA))
async def process_add_user_callback(call: CallbackQuery, callback_data) -> None:
    await bot.send_message(
        call.from_user.id,
        UserAddMessages.USER_ADD_MESSAGE.value
    )
    await bot.send_message(
        call.from_user.id,
        UserAddMessages.USER_ADD_MESSAGE_FILLING_NAME.value,
        reply_markup=get_stop_filling_keyboard()
    )
    await FillEmployee.name.set()


@dp.message_handler(commands=["user_add"])
async def process_add_user_command(message: types.Message):
    await message.answer(
        UserAddMessages.USER_ADD_MESSAGE.value
    )
    await message.answer(
        UserAddMessages.USER_ADD_MESSAGE_FILLING_NAME.value,
        reply_markup=get_stop_filling_keyboard()
    )
    await FillEmployee.name.set()


@dp.message_handler(lambda message: message.text == STOP_FILLING, state="*")
async def stop_filling(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        UserAddMessages.USER_ADD_MESSAGE_FILLING_STOPPED.value,
        reply_markup=get_main_keyboard()
    )


@dp.message_handler(state=FillEmployee.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(
        UserAddMessages.USER_ADD_MESSAGE_FILLING_PATRONYMIC.value,
        reply_markup=get_optional_field_keyboard()
    )
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.patronymic)
async def process_patronymic(message: types.Message, state: FSMContext):
    patronymic = message.text
    await state.update_data(patronymic=patronymic)
    await message.answer(
        UserAddMessages.USER_ADD_MESSAGE_FILLING_SURNAME.value,
        reply_markup=get_stop_filling_keyboard()
    )
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.surname)
async def process_surname(message: types.Message, state: FSMContext):
    surname = message.text
    await state.update_data(surname=surname)
    await message.answer(UserAddMessages.USER_ADD_MESSAGE_FILLING_JOB_TITLE.value)
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.job_title)
async def process_job_title(message: types.Message, state: FSMContext):
    job_title = message.text
    await state.update_data(job_title=job_title)
    await message.answer(UserAddMessages.USER_ADD_MESSAGE_FILLING_PROJECT.value)
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.project)
async def process_project(message: types.Message, state: FSMContext):
    project = message.text
    await state.update_data(project=project)
    await message.answer(
        UserAddMessages.USER_ADD_MESSAGE_FILLING_AVATAR.value,
        reply_markup=get_optional_field_keyboard()
    )
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.avatar_path, content_types=types.ContentType.PHOTO)
async def process_avatar(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    file_id = photo.file_id

    file_name = f'{str(uuid.uuid4())}.jpg'
    full_file_path = Path(TEMP_STATIC_PATH) / file_name

    await bot.download_file_by_id(file_id, full_file_path)

    await state.update_data(avatar_path=full_file_path)
    await message.answer(
        UserAddMessages.USER_ADD_MESSAGE_FILLING_DONE.value,
        reply_markup=get_main_keyboard()
    )
    await EmployeesService.new(state)
    await state.finish()

