from typing import Union

"""аннотируем тип переменной"""


def get_mask_card_number(сard_number: Union[str]) -> str:
    """маскируем номер банковской карты"""

    card_number_spaceless = сard_number.replace(" ", "")
    """убираем возможные пробелы"""

    if len(card_number_spaceless) != 16:
        return "Номер карты должен содержать 16 цифр."

    if not card_number_spaceless.isdigit():
        return "Номер карты должен содержать только цифры."

    first_part_card = card_number_spaceless[:4]
    second_part_card = card_number_spaceless[4:6]
    third_part_card = "**"
    fourth_part_card = "****"
    fifth_part_card = card_number_spaceless[12:16]

    """определяем, какие части карты будут замаскированы"""

    masked_number_card = (
        f"{first_part_card} {second_part_card}{third_part_card} " f"{fourth_part_card} {fifth_part_card}"
    )

    """складываем части карты вместе"""

    return masked_number_card


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: Union[str]) -> str:
    """маскируем номер банковского счета"""

    account_number_spaceless = account_number.replace(" ", "")
    """убираем возможные пробелы"""

    if len(account_number_spaceless) != 20:
        return "Номер аккаунта должен содержать 20 цифр."

    if not account_number_spaceless.isdigit():
        return "Номер аккаунта должен содержать только цифры."

    first_part_account = "**"
    second_part_account = account_number_spaceless[-4:]

    """определяем, какие части аккаунта будут замаскированы"""

    masked_number_account = f"{first_part_account} {second_part_account}"

    """складываем части аккаунта вместе"""

    return masked_number_account


print(get_mask_account("73654108430135874305"))
