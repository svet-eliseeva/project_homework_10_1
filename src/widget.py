def mask_account_card(card: str) -> str:
    '''Функция маскировки номера банковского счета либо карты'''
    if 'Счет' in card:
        return f'{card[:5]}**{card[-4:]}'
    else:
        return f'{card[:-12]} {card[-12:-10]}** **** {card[-4:]}'


print(mask_account_card("Maestro 1596837868705199"))


def get_date(date_: str) -> str:
    """Функция, которая меняет формат даты"""
    # "2024-03-11T02:26:18.671407"
    return f'{date_[8:10]}.{date_[5:7]}.{date_[:4]}'


# "ДД.ММ.ГГГГ" "11.03.2024"
print(get_date("2024-03-11T02:26:18.671407"))
