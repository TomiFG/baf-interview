from quote_api.utils import get_applicable_rate

def test_get_applicable_rate(routes) -> None:
    rates = routes[0].rates
    assert get_applicable_rate(rates, 14.625) == 5.0

def test_get_applicable_rate_2(routes) -> None:
    rates = routes[2].rates
    assert get_applicable_rate(rates, 44.2) == 8.0

def test_get_applicable_rate_too_light(routes) -> None:
    rates = routes[1].rates
    assert get_applicable_rate(rates, 99) == None

def test_get_applicable_rate_on_the_limit(routes) -> None:
    rates = routes[0].rates
    assert get_applicable_rate(rates, 10000) == None


