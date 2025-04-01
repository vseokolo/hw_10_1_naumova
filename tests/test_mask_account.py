from src.mask import get_mask_account
import pytest

@pytest.mark.parametrize('account_number, expected',
                         [
                             ('73654108430135874305', '** 4305'),
                             ('49248242942040240130', '** 0130'),
                             ('00000000000000000000', '** 0000'),
                             ('10101010100222222222', '** 2222')
                         ])

def test_get_mask_account(account_number: str, expected: str):
    """используем параматризацию для проверки сразу нескольких тестов"""
    assert get_mask_account(account_number) == expected

    with pytest.raises(ValueError) as exc_info:
        get_mask_account('111')

    with pytest.raises(ValueError) as exc_info:
        get_mask_account('aaa')

    with pytest.raises(TypeError) as exc_info:
        get_mask_account('aaaa1111бббm---ß,,,p')

    with pytest.raises(ValueError) as exc_info:
        get_mask_account('')