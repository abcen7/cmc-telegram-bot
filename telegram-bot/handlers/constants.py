from enum import Enum, auto

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


class SearchType(Enum):
    NAME = "name"
    SURNAME = "surname"
    PROJECT = "project"
    JOB_TITLE = "job_title"


class SearchResultMessages(Enum):
    SEARCH_RESULT_NOT_FOUND = "[🔎] Поиск не дал никакого ответа ..."


class UserSearchMessages(Enum):
    USER_SEARCH_MESSAGE = """
    🔎 Давайте найдем пользователя...
    Выберете, по какой характеристике его искать ниже
    """
    USER_SEARCH_WAITING = "Бот уже ищет сотрудника!"
    USER_SEARCH_ASK = "[💬] Введите данные: "


API_TO_RESULT = {
    '_id': '<b>ID</b>: ',
    'name': '<b>Имя</b>: ',
    'patronymic': '<b>Отчество</b>: ',
    'surname': '<b>Фамилия</b>: ',
    'job_title': '<b>Должность</b>: ',
    'project': '<b>Проект</b>: '
}

NEW_LINE = "\n"
AVATAR_PATH = 'avatar_path'
CREATED = 'created'
