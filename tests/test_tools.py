# tests/test_tools.py
from process.functional_tools import total_sleep_time

def test_total_sleep_time():
    data = [{'duration': 30}, {'duration': 60}, {'duration': 90}]
    assert total_sleep_time(data) == 180
