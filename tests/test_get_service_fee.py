from quote_api.utils import get_service_fee

def test_get_service_fee():
    assert get_service_fee({'service_fee': 300}) == 300

def test_get_service_fee_null():
    assert get_service_fee({}) == 0

def test_get_service_fee_2():
    assert get_service_fee({'service_fee': 2}) == 2