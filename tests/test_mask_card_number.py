import pytest

from src.mask import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("8429482403109324", "8429 48** **** 9324"),
        ("0000000100001001", "0000 00** **** 1001"),
        ("0000066666666666", "0000 06** **** 6666"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str):
    """используем параматризацию для проверки сразу нескольких тестов"""
    assert get_mask_card_number(card_number) == expected

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("111")

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("aaa")

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number("aaaa1111бббm---ß")

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
