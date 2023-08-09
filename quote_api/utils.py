import json

from quote_api import db, app
from quote_api.models import ShippingRoute, CostBreakdown, Box, Quote

def get_service_fee(rules: dict) -> float:
    return rules.get('service_fee', 0.0) if rules else 0.0

def get_oversize_fee(box: Box, rules: dict) -> float:
    limit = rules.get('oversize_limit', 120) if rules else 120
    oversize_fee = 100.0 if max(box.height, box.lenght, box.width) > limit else 0.0
    return oversize_fee 

def get_overweight_fee(box: Box, rules: dict) -> float:
    limit = rules.get('overweight_limit', 30) if rules else 30
    overweight_fee = 80.0 if box.weight_kg > limit else 0.0
    return overweight_fee 

def get_applicable_rate(rates: list, weight: float) -> float | None:
    for rate in rates:
        if weight > rate['min_weight_kg'] and weight < rate['max_weight_kg']:
            return rate['per_kg_rate']
    return None

def get_quote(route: ShippingRoute, boxes: list[Box]) -> Quote:

    total_chargeable_weight = 0
    oversize_fees = 0
    overweight_fees = 0

    for box in boxes:
        total_chargeable_weight += box.chargable_weight * box.count
        oversize_fees += get_oversize_fee(box, route.special_rules) * box.count
        print(f'box weight: {route.special_rules}. of_total: {oversize_fees}')
        overweight_fees += get_overweight_fee(box, route.special_rules) * box.count

    rate = get_applicable_rate(route.rates, total_chargeable_weight)

    if not rate:
        return 

    cost_breakdown = CostBreakdown(
        shipping_cost=rate * total_chargeable_weight,
        service_fee=get_service_fee(route.special_rules),
        oversize_fee=oversize_fees,
        overweight_fee=overweight_fees
    )

    quote = Quote(
        shipping_channel=route.shipping_channel,
        total_cost=cost_breakdown.total_cost,
        cost_breakdown=cost_breakdown,
        shipping_time_range=route.shipping_time_range
    )
        
    return quote


def read_rates_file(path):
    with open(path, 'r') as rates_file:
        routes_data = json.loads(rates_file.read())

    routes = []
    for i, route in enumerate(routes_data):

        special_rules = {}
        if route['starting_country'] == 'China':
            special_rules['service_fee'] = 300
        elif route['starting_country'] == 'India':
            special_rules['overweight_limit'] = 15
        elif route['starting_country'] == 'Vietnam':
            special_rules['oversize_limit'] = 70 

        shipping_route = ShippingRoute(
            id=i,
            starting_country=route['starting_country'],
            destination_country=route['destination_country'],
            shipping_channel=route['shipping_channel'],
            shipping_time_range=route['shipping_time_range'],
            rates=route['rates'],
            special_rules=special_rules
        )

        routes.append(shipping_route)

    return routes

def setup_database():

    with app.app_context():
        
        db.create_all()
        routes = read_rates_file('aux_files/rates.json')
        for shipping_route in routes:
            db.session.add(shipping_route)
        db.session.commit()
