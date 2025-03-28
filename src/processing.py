from typing import Dict, List

"""аннотируем тип переменных"""


def filter_by_state(dictionary_info: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """определяем функцию для фильтрования операций по статусу"""
    return [item for item in dictionary_info if item.get("state") == state]


print(
    filter_by_state(
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
)


def sort_by_date(
    dictionary_info: List[Dict],
) -> List[Dict]:
    """определяем функцию для фильтрования операций по дате"""
    return sorted(dictionary_info, key=lambda item: item["date"], reverse=True)


"""определяем функцию для фильтрования операций по дате"""

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
