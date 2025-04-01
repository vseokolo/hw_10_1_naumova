from typing import Dict, List
from src.processing import filter_by_state, operations_data, operations_data_sorted
import pytest

@pytest.mark.parametrize('state, expected',
                         [
                             (operations_data, operations_data_sorted)
                         ])

def test_filter_by_state(state: str, expected: List[Dict]):
    """используем параматризацию для проверки сразу нескольких тестов"""
    assert filter_by_state(state) == expected

with pytest.raises(TypeError) as exc_info:

    test_filter_by_state('20-03-11T02:26:18.671407')

with pytest.raises(TypeError) as exc_info:
    test_filter_by_state('01-2000-01T09:56:09.000430')

with pytest.raises(TypeError) as exc_info:
    test_filter_by_state('')
