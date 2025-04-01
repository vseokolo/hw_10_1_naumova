from datetime import datetime

"""импортируем модуль datetime"""


def mask_account_card(card_info: str) -> str:
    """Создаём функцию, принимающая информацию о карте в виде строки"""
    if len(card_info) < 16:
        raise ValueError("Номер карты или счета не может быть меньше 16")
    if not card_info[-16:].isdigit():
        raise TypeError("Номер карты или счета должен содержать только цифры.")

    if "Счет" in card_info:
        if len(card_info) < 25:
            raise ValueError("Номер счета не может быть меньше 20")
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


print(mask_account_card("Счет 00001111393920490000"))


def get_date(user_date: str) -> str:
    """определяем функцию для получения даты"""

    user_year = datetime.strptime(user_date[:10], "%Y-%m-%d").year
    user_month = datetime.strptime(user_date[:10], "%Y-%m-%d").month
    user_day = datetime.strptime(user_date[:10], "%Y-%m-%d").day
    """получаем год, месяц и день из строки пользователя"""

    def validate_date(user_date):
        try:
            datetime.strptime(user_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна соответствовать формату %Y-%m-%d")

    return f"{user_day:02}.{user_month:02}.{user_year}"


print(get_date("2200-12-31T07:59:10.000001"))
