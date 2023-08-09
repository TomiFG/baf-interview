from quote_api import db
from quote_api.models import ShippingRoute

def get_shipping_routes(starting_country: str, destination_country: str) -> list[ShippingRoute]:
    shipping_routes = db.session.query(ShippingRoute).where(
                                    db.and_(ShippingRoute.starting_country == starting_country,
                                            ShippingRoute.destination_country == destination_country)).all()
    return shipping_routes