from aiogram.types import CallbackQuery

from handlers.constants import UserAddMessages
from keyboards.constants import USER_SEARCH_DATA
from keyboards.executor import executor_cb, get_stop_filling_keyboard
from main import bot, dp


@dp.callback_query_handler(executor_cb.filter(action=USER_SEARCH_DATA))
async def process_search_employee_callback(call: CallbackQuery, callback_data) -> None:
    await bot.send_message(
        call.from_user.id,
        UserAddMessages.USER_ADD_MESSAGE.value
    )
    await bot.send_message(
        call.from_user.id,
        UserAddMessages.USER_ADD_MESSAGE_FILLING_NAME.value,
        reply_markup=get_stop_filling_keyboard()
    )
