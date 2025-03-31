from audioop import reverse

from src.processing import operations_data, operations_data_sorted_date, sort_by_date

import pytest

@pytest.mark.parametrize('date, expected',
                         [
                             (operations_data, operations_data_sorted_date)
                         ])
def test_sort_by_date(date, expected):
    assert sort_by_date(date) == expected

