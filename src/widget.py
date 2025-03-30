from datetime import datetime

"""импортируем модуль datetime"""


def mask_account_card(card_info: str) -> str:
    """Создаём функцию, принимающая информацию о карте в виде строки"""

    if "Счет" in card_info:
        first_part_account = "**"
        second_part_account = card_info[-4:]
        """определяем, какие части аккаунта будут замаскированы"""
        card_info = f"Счет {first_part_account}{second_part_account}"
        """складываем части аккаунта вместе"""
        return card_info

    else:
        first_part_card = card_info[:-12]
        second_part_card = card_info[-12:-10]
        third_part_card = "**"
        fourth_part_card = "****"
        fifth_part_card = card_info[-4:]

        """определяем, какие части карты будут замаскированы"""

        card_info = f"{first_part_card} {second_part_card}{third_part_card} " f"{fourth_part_card} {fifth_part_card}"

        """складываем части карты вместе"""

        return card_info


print(mask_account_card("Счет 0000111139392049"))


def get_date(user_date: str) -> str:
    """определяем функцию для получения даты"""

    user_year = datetime.strptime(user_date[:10], "%Y-%m-%d").year
    user_month = datetime.strptime(user_date[:10], "%Y-%m-%d").month
    user_day = datetime.strptime(user_date[:10], "%Y-%m-%d").day
    """получаем год, месяц и день из строки пользователя"""

    return f"{user_day:02}.{user_month:02}.{user_year}"


print(get_date("2200-12-31T07:59:10.000001"))
