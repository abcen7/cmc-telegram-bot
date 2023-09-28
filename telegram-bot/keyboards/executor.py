from typing import List, Dict

from aiogram.types import \
    InlineKeyboardButton, \
    InlineKeyboardMarkup, \
    ReplyKeyboardMarkup, \
    KeyboardButton

from aiogram.utils.callback_data import CallbackData

from keyboards.constants import \
    COMMANDS_MESSAGE, \
    OPTIONAL_FIELD, \
    STOP_FILLING_FIELD, \
    DONT_UPDATE_FIELD, \
    EmployeeSearchButtons, \
    EmployeeCardActionsButtons, \
    EmployeeMainButtons

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
                    text=EmployeeMainButtons.ADD_TEXT.value,
                    callback_data=executor_cb.new(
                        action=EmployeeMainButtons.ADD_DATA.value
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EmployeeMainButtons.UPDATE_TEXT.value,
                    callback_data=executor_cb.new(
                        action=EmployeeMainButtons.UPDATE_DATA.value
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EmployeeMainButtons.DELETE_TEXT.value,
                    callback_data=executor_cb.new(
                        action=EmployeeMainButtons.DELETE_DATA.value
                    ),
                )
            ],
            [
                InlineKeyboardButton(
                    text=EmployeeMainButtons.SEARCH_TEXT.value,
                    callback_data=executor_cb.new(
                        action=EmployeeMainButtons.SEARCH_DATA.value
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
        KeyboardButton(STOP_FILLING_FIELD)
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


async def get_employees_list_keyboard(employees: List[Dict[str, str]]) -> InlineKeyboardMarkup:
    buttons = []
    for employee in employees:
        buttons.append(
            [
                InlineKeyboardButton(
                    f"...{employee['_id'][-5:]} {employee['name']} {employee['surname']} {employee['project']}",
                    callback_data=f"employee_info_{employee['_id']}"
                )
            ]
        )
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=buttons)