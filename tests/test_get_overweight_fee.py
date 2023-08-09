import pytest

from quote_api.models import Box
from quote_api.utils import get_overweight_fee

@pytest.mark.parametrize('box,overweight_fee', [
    (Box(4, 10, 50, 50, 50), 0),
    (Box(4, 31, 50, 121, 50), 80),
    (Box(8, 30, 120, 120, 120), 0),
    (Box(100, 500, 0, 0, 0), 80),
])
def test_get_overweight_fee_standard(box, overweight_fee):
    assert get_overweight_fee(box, {}) == overweight_fee

@pytest.mark.parametrize('box,rules,overweight_fee', [
    (Box(4, 16, 100, 165, 150),{'overweight_limit':15}, 80),
    (Box(4, 10, 100, 165, 150),{'overweight_limit':15}, 0),
    (Box(1, 155, 50, 50, 50),{'overweight_limit':150}, 80),
    (Box(5, 145, 40, 40, 40),{'overweight_limit':150}, 0),
    (Box(100, 45, 46, 0, 0),{'overweight_limit':45}, 0),
])
def test_get_overweight_fee_special_rules(box,rules, overweight_fee):
    assert get_overweight_fee(box, rules) == overweight_fee