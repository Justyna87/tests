import pytest
from evaluate_function import evaluate

# test for no winners
def test_evaluate():
    result = evaluate("oxoxoxoxoxoxoxox-oox")
    assert result == False