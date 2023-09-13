from enum import Enum

WELCOME_MESSAGE = """
Привет 👋

👁️‍🗨️ Я Users Management Bot написанный @abcen7
⚒️ Я упрощаю управление информацией о сотрудниках.
⚡️ Я предоставляю удобный интерфейс для добавления, удаления, редактирования и поиска сотрудников.
"""

HELP_MESSAGE = """
Список моих команд
- /user_add
- /user_remove
- /user_search
"""


class UserAddMessages(Enum):
    USER_ADD_MESSAGE = """🪪 Давайте заполним карточку нового сотрудника!"""
    USER_ADD_MESSAGE_CANCEL = """❌ Вы отменили создание нового сотрудника"""
    USER_ADD_MESSAGE_FILLING_NAME = "💬 Введите имя"
    USER_ADD_MESSAGE_FILLING_SURNAME = "💬 Введите фамилию"
    USER_ADD_MESSAGE_FILLING_PATRONYMIC = "💬 Введите отчество (Опционально)"
    USER_ADD_MESSAGE_FILLING_JOB_TITLE = "💬 Введите должность"
    USER_ADD_MESSAGE_FILLING_PROJECT = "💬 Введите проект сотрудника"
    USER_ADD_MESSAGE_FILLING_AVATAR = "💬 Прикрепите аватарку сотрудника (Опционально)"
    USER_ADD_MESSAGE_FILLING_DONE = "✅ Отлично! Вы успешно создали пользователя!"
    USER_ADD_MESSAGE_FILLING_STOPPED = "❌ Заполнение прервано. Все данные сброшены."


class UserSearchMessages(Enum):
    USER_SEARCH_MESSAGE = """
    🔎 Давайте найдем пользователя...
    Выберете, по какой характеристике его искать ниже
    """
    USER_SEARCH_NAME = "Имя"
    USER_SEARCH_SURNAME = "Фамилия"
    USER_SEARCH_PATRONYMIC = "Отчество"
    USER_SEARCH_PROJECT = "Проект"
    USER_SEARCH_JOB_TITLE = "Должность"
