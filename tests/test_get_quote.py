from quote_api.utils import get_quote
from quote_api.models import CostBreakdown, Quote

def test_get_quote_china_air(routes, boxes):
    shipping_route = routes[0] # China air
    quote = get_quote(shipping_route, boxes)
    expected_cost_breakdown = CostBreakdown(
        shipping_cost=934.5,
        service_fee=300
    )

    expected_quote = Quote(
        shipping_channel='air',
        total_cost=1234.5,
        cost_breakdown=expected_cost_breakdown,
        shipping_time_range={
                                "min_days": 15,
                                "max_days": 20
                            }
    )
    assert quote == expected_quote

def test_get_quote_india_air(routes, boxes):
    shipping_route = routes[2] # India air
    quote = get_quote(shipping_route, boxes)
    expected_cost_breakdown = CostBreakdown(
        shipping_cost=1602.0,
        overweight_fee=800.0
    )

    expected_quote = Quote(
        shipping_channel='air',
        total_cost=2402.0,
        cost_breakdown=expected_cost_breakdown,
        shipping_time_range={
                                "min_days": 10,
                                "max_days": 15
                            }
    )
    assert quote == expected_quote

def test_get_quote_vietnam_air(routes, boxes):
    shipping_route = routes[4] # Vietnam air
    quote = get_quote(shipping_route, boxes)
    expected_cost_breakdown = CostBreakdown(
        shipping_cost=1068.0,
        oversize_fee=600.0
    )

    expected_quote = Quote(
        shipping_channel='air',
        total_cost=1668.0,
        cost_breakdown=expected_cost_breakdown,
        shipping_time_range={
                                "min_days": 0,
                                "max_days": 100
                            }
    )
    assert quote == expected_quote