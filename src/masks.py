from typing import Any


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card = str(card_number)

    return f'{card[:4]} {card[5:7]}** **** {card[-4:]}'


print(get_mask_card_number(7000792289606361))


def get_mask_account(account: int) -> str:
    """Функция маскировки номера банковского счета"""
    mask_account = str(account)
    return f'**{mask_account[-4:]}'


print(get_mask_account(73654108430135874305))
