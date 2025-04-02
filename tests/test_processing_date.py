from typing import Dict, List

import pytest

from src.processing import operations_data, operations_data_sorted_date, sort_by_date


@pytest.mark.parametrize("date, expected", [(operations_data, operations_data_sorted_date)])
def test_sort_by_date(date: List[Dict], expected: List[Dict]):
    """используем параматризацию для проверки сразу нескольких тестов"""
    assert sort_by_date(date) == expected
