from typing import Dict, List

"""аннотируем тип переменных"""


operations_data = [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
"""создаем переменную operations_data для данных на вход"""

def filter_by_state(dictionary_info: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """определяем функцию для фильтрования операций по статусу"""
    def validate_date(user_date):
        try:
            datetime.strptime(user_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Дата должна соответствовать формату %Y-%m-%d')
    return [item for item in dictionary_info if item.get("state") == state]

operations_data_sorted = filter_by_state((operations_data))
"""создаем переменную operations_data_sorted для отфильтрованных данных на выход"""
print(operations_data_sorted)


def sort_by_date(
    dictionary_info: List[Dict],
) -> List[Dict]:
    """определяем функцию для фильтрования операций по дате"""
    return sorted(dictionary_info, key=lambda item: item["date"], reverse=True)

"""определяем функцию для фильтрования операций по дате"""

operations_data_sorted_date = sort_by_date(operations_data)
print(operations_data_sorted_date)
