from aiogram.types import \
    InlineKeyboardButton, \
    InlineKeyboardMarkup, \
    ReplyKeyboardMarkup, \
    KeyboardButton

from aiogram.utils.callback_data import CallbackData

from keyboards.constants import \
    COMMANDS_MESSAGE, \
    USER_ADD_TEXT, \
    USER_REMOVE_TEXT, \
    USER_SEARCH_TEXT, \
    OPTIONAL_FIELD, \
    STOP_FILLING

from keyboards.constants import \
    USER_ADD_DATA, \
    USER_REMOVE_DATA, \
    USER_SEARCH_DATA

executor_cb = CallbackData("executor", "action")


def get_main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(COMMANDS_MESSAGE)
    )


def get_commands_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=USER_ADD_TEXT,
                    callback_data=executor_cb.new(
                        action=USER_ADD_DATA
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=USER_REMOVE_TEXT,
                    callback_data=executor_cb.new(
                        action=USER_REMOVE_DATA
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=USER_SEARCH_TEXT,
                    callback_data=executor_cb.new(
                        action=USER_SEARCH_DATA
                    ),
                )
            ],
        ],
    )


def get_optional_field_keyboard() -> InlineKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(OPTIONAL_FIELD)
    )


def get_stop_filling_keyboard() -> InlineKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(STOP_FILLING)
    )
