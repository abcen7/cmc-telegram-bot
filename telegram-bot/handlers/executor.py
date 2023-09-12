from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

import services
from handlers.constants import UserAddMessages
from handlers.default import process_commands_button
from keyboards.executor import executor_cb
from main import bot, dp

from keyboards.constants import \
    USER_ADD_DATA


class FillEmployee(StatesGroup):
    name = State()
    patronymic = State()
    surname = State()
    job_title = State()
    project = State()
    avatar = State()


@dp.callback_query_handler(executor_cb.filter(action=USER_ADD_DATA))
async def process_add_user_callback(call: CallbackQuery, callback_data) -> None:
    await bot.send_message(
        call.from_user.id,
        UserAddMessages.USER_ADD_MESSAGE.value
    )
    await FillEmployee.name.set()


@dp.message_handler(state=FillEmployee.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.reply(UserAddMessages.USER_ADD_MESSAGE_FILLING_PATRONYMIC.value)
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.patronymic)
async def process_patronymic(message: types.Message, state: FSMContext):
    patronymic = message.text
    await state.update_data(patronymic=patronymic)
    await message.reply(UserAddMessages.USER_ADD_MESSAGE_FILLING_SURNAME.value)
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.surname)
async def process_surname(message: types.Message, state: FSMContext):
    surname = message.text
    await state.update_data(surname=surname)
    await message.reply(UserAddMessages.USER_ADD_MESSAGE_FILLING_JOB_TITLE.value)
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.job_title)
async def process_job_title(message: types.Message, state: FSMContext):
    job_title = message.text
    await state.update_data(job_title=job_title)
    await message.reply(UserAddMessages.USER_ADD_MESSAGE_FILLING_PROJECT.value)
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.project)
async def process_project(message: types.Message, state: FSMContext):
    project = message.text
    await state.update_data(project=project)
    await message.reply(UserAddMessages.USER_ADD_MESSAGE_FILLING_AVATAR.value)
    await FillEmployee.next()


@dp.message_handler(state=FillEmployee.avatar)
async def process_avatar(message: types.Message, state: FSMContext):
    avatar = message.text
    await state.update_data(avatar=avatar)
    await message.reply(UserAddMessages.USER_ADD_MESSAGE_FILLING_DONE.value)
    # await services.UserService.new(state)
    print(state.get_data())
    await state.finish()
