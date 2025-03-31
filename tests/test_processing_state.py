from typing import Dict, List
from src.processing import filter_by_state, operations_data, operations_data_sorted

import pytest

@pytest.mark.parametrize('state, expected',
                         [
                             (operations_data, operations_data_sorted)
                         ])


def test_filter_by_state(state: str, expected: List[Dict]):
    assert filter_by_state(state) == expected

