from src.widget import get_date
from datetime import datetime

import pytest

@pytest.mark.parametrize('user_date, expected',
                         [
                             ('2024-03-11T02:26:18.671407', '11.03.2024'),
                             ('1905-01-09T17:00:00.000000', '09.01.1905'),
                             ('2000-01-01T09:56:09.000430', '01.01.2000'),
                             ('2200-12-31T07:59:10.000001', '31.12.2200')
                         ])
def test_widget_get_date(user_date: str, expected:str):
    """используем параматризацию для проверки сразу нескольких тестов"""
    assert get_date(user_date) == expected

with pytest.raises(TypeError) as exc_info:

    test_widget_get_date('20-03-11T02:26:18.671407')

with pytest.raises(TypeError) as exc_info:
    test_widget_get_date('01-2000-01T09:56:09.000430')

with pytest.raises(TypeError) as exc_info:
    test_widget_get_date('')