from enum import Enum

COMMANDS_MESSAGE = "🔑 Команды"

EMPLOYEE_ADD_TEXT = "🆕 Создать карточку сотрудника"
EMPLOYEE_UPDATE_TEXT = "✍️ Обновить карточку сотрудника"
EMPLOYEE_DELETE_TEXT = "❌️ Удалить карточку сотрудника"
EMPLOYEE_SEARCH_TEXT = "👀 Найти карточку сотрудника"

EMPLOYEE_ADD_DATA = "employee_add"
EMPLOYEE_UPDATE_DATA = "employee_update"
EMPLOYEE_REMOVE_DATA = "employee_remove"
EMPLOYEE_SEARCH_DATA = "employee_search"


class EmployeeSearchButtons(Enum):
    NAME_TEXT = "[🔎] Поиск по имени"
    SURNAME_TEXT = "[🔎] Поиск по фамилии"
    JOB_TITLE_TEXT = "[🔎] Поиск по должности"
    PROJECT_TEXT = "[🔎] Поиск по проекту"
    NAME_DATA = "employee_search_name"
    SURNAME_DATA = "employee_search_surname"
    JOB_TITLE_DATA = "employee_search_job_title"
    PROJECT_DATA = "employee_search_project"


OPTIONAL_FIELD = "🚫 Не указывать"
DONT_UPDATE_FIELD = "🚫 Оставить текущее значение"
STOP_FILLING = "🚫 Остановить заполнение"
