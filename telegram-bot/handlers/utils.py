import datetime
from typing import Dict, List

from handlers.constants import SearchResultMessages, API_TO_RESULT, NEW_LINE, AVATAR_PATH, CREATED


async def get_result_or_failed(employees: List[Dict[str, str]]) -> List[str]:
    print(employees)
    if len(employees) == 0:
        return SearchResultMessages.SEARCH_RESULT_NOT_FOUND.value
    else:
        employee_cards = []
        for employee in employees[:5]:
            employee_card = []
            for key in employee:
                if key == AVATAR_PATH:
                    employee_card.append(f'<a href="{employee[key]}">&#8205;</a>')
                if key == CREATED:
                    print(datetime.datetime.fromtimestamp(employee[key]))
                    employee_card.append(f'<b>Дата прихода</b>: {datetime.datetime.fromtimestamp(employee[key])}')
                if key in API_TO_RESULT:
                    employee_card.append(str(API_TO_RESULT[key]) + str(employee[key]))
            employee_cards.append(NEW_LINE.join(employee_card))
        return employee_cards
