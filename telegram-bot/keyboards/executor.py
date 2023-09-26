from aiogram.types import \
    InlineKeyboardButton, \
    InlineKeyboardMarkup, \
    ReplyKeyboardMarkup, \
    KeyboardButton

from aiogram.utils.callback_data import CallbackData

from keyboards.constants import \
    COMMANDS_MESSAGE, \
    EMPLOYEE_ADD_TEXT, \
    EMPLOYEE_DELETE_TEXT, \
    EMPLOYEE_SEARCH_TEXT, \
    OPTIONAL_FIELD, \
    STOP_FILLING, \
    EMPLOYEE_UPDATE_TEXT, \
    EMPLOYEE_UPDATE_DATA, \
    DONT_UPDATE_FIELD, \
    EmployeeSearchButtons, \
    EmployeeCardActionsButtons

from keyboards.constants import \
    EMPLOYEE_ADD_DATA, \
    EMPLOYEE_REMOVE_DATA, \
    EMPLOYEE_SEARCH_DATA

executor_cb = CallbackData("executor", "action")
employee_cb = CallbackData("employee", "employee_id", "action")


def get_main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(COMMANDS_MESSAGE)
    )


def get_commands_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=EMPLOYEE_ADD_TEXT,
                    callback_data=executor_cb.new(
                        action=EMPLOYEE_ADD_DATA
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EMPLOYEE_UPDATE_TEXT,
                    callback_data=executor_cb.new(
                        action=EMPLOYEE_UPDATE_DATA
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EMPLOYEE_DELETE_TEXT,
                    callback_data=executor_cb.new(
                        action=EMPLOYEE_REMOVE_DATA
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EMPLOYEE_SEARCH_TEXT,
                    callback_data=executor_cb.new(
                        action=EMPLOYEE_SEARCH_DATA
                    ),
                )
            ],
        ],
    )


def get_optional_and_dont_update_keyboard() -> InlineKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(OPTIONAL_FIELD)
    ).add(
        KeyboardButton(DONT_UPDATE_FIELD)
    )


def get_optional_field_keyboard() -> InlineKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(OPTIONAL_FIELD)
    )


def get_dont_update_field_keyboard() -> InlineKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(DONT_UPDATE_FIELD)
    )


def get_stop_filling_keyboard() -> InlineKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(STOP_FILLING)
    )


def get_employee_card_actions_keyboard(employee_id) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=EmployeeCardActionsButtons.EDIT_TEXT.value,
                    callback_data=employee_cb.new(
                        action=EmployeeCardActionsButtons.EDIT_DATA.value,
                        employee_id=employee_id
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EmployeeCardActionsButtons.DELETE_TEXT.value,
                    callback_data=employee_cb.new(
                        action=EmployeeCardActionsButtons.DELETE_DATA.value,
                        employee_id=employee_id
                    ),
                )
            ],
        ],
    )


def get_search_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=EmployeeSearchButtons.NAME_TEXT.value,
                    callback_data=executor_cb.new(
                        action=EmployeeSearchButtons.NAME_DATA.value
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EmployeeSearchButtons.SURNAME_TEXT.value,
                    callback_data=executor_cb.new(
                        action=EmployeeSearchButtons.SURNAME_DATA.value
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EmployeeSearchButtons.PROJECT_TEXT.value,
                    callback_data=executor_cb.new(
                        action=EmployeeSearchButtons.PROJECT_DATA.value
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EmployeeSearchButtons.JOB_TITLE_TEXT.value,
                    callback_data=executor_cb.new(
                        action=EmployeeSearchButtons.JOB_TITLE_DATA.value
                    ),
                )
            ],
        ],
    )
