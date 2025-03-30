from src.widget import mask_account_card

import pytest

@pytest.mark.parametrize('card_info, expected',
                         [
                             ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                             ('Visa 0000000000000000', 'Visa 0000 00** **** 0000'),
                             ('Счет 0000111139392049', 'Счет **2049'),
                             ('Maestro 0000111139392049', 'Maestro 0000 11** **** 2049')
                         ])
def test_widget_mask_account_card(card_info, expected):
    assert mask_account_card(card_info) == expected
