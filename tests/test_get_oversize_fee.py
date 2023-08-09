import pytest

from quote_api.models import Box
from quote_api.utils import get_oversize_fee

@pytest.mark.parametrize('box,oversize_fee', [
    (Box(4, 10, 121, 50, 50), 100),
    (Box(4, 10, 50, 121, 50), 100),
    (Box(4, 10, 50, 50, 121), 100),
    (Box(4, 10, 121, 50, 150), 100),
    (Box(4, 10, 50, 50, 50), 0),
    (Box(4, 10, 120, 120, 120), 0),
    (Box(100, 500, 0, 0, 0), 0),
])
def test_get_oversize_fee_standard(box, oversize_fee):
    assert get_oversize_fee(box, {}) == oversize_fee

@pytest.mark.parametrize('box,rules,oversize_fee', [
    (Box(4, 10, 50, 50, 71),{'oversize_limit':70}, 100),
    (Box(4, 10, 50, 50, 50),{'oversize_limit':70}, 0),
    (Box(4, 10, 70, 70, 70),{'oversize_limit':70}, 0),
    (Box(4, 10, 100, 165, 150),{'oversize_limit':150}, 100),
    (Box(4, 10, 145, 145, 145),{'oversize_limit':150}, 0),
    (Box(4, 10, 40, 40, 40),{'oversize_limit':45}, 0),
    (Box(100, 500, 46, 0, 0),{'oversize_limit':45}, 100),
])
def test_get_oversize_fee_special_rules(box,rules, oversize_fee):
    assert get_oversize_fee(box, rules) == oversize_fee