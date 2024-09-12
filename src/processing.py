from typing import Any


def filter_by_state(list_d: list[dict[str, Any]], state_default: str = 'EXECUTED') -> list[dict[str, Any]]:
    """ Функция возврата списка словарей по заданному ключу state(состояние) по умолчанию 'EXECUTED'(выполнено)"""
    new_list_state = []
    for key in list_d:
        if key.get('state') == state_default:
            new_list_state.append(key)
    return new_list_state


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                      ))


def sort_by_date(list_state: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует список словарей по дате по убыванию"""
    sorted_list_state = sorted(list_state, key=lambda x: x["date"], reverse=reverse)

    return sorted_list_state


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                   ))
