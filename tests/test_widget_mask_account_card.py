import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "card_info, expected",
    [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa 0000000000000000", "Visa 0000 00** **** 0000"),
        ("Счет 00000000000000000000", "Счет **0000"),
        ("Maestro 0000111139392049", "Maestro 0000 11** **** 2049"),
    ],
)
def test_widget_mask_account_card(card_info: str, expected: str):
    """используем параматризацию для проверки сразу нескольких тестов"""
    assert mask_account_card(card_info) == expected

    with pytest.raises(ValueError) as exc_info:
        mask_account_card("111000099998888")

    with pytest.raises(TypeError) as exc_info:
        mask_account_card("aaaa1111бббm---ß,,,p")

    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")

    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Счет 7158300734726758")
