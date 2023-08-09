from dataclasses import dataclass
from quote_api import db


@dataclass
class ShippingRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starting_country = db.Column(db.String, nullable=False)
    destination_country = db.Column(db.String, nullable=False)
    shipping_channel = db.Column(db.String, nullable=False)
    shipping_time_range = db.Column(db.JSON, nullable=False)
    rates = db.Column(db.JSON, nullable=False)

    special_rules = db.Column(db.JSON)


@dataclass
class Box:
    count: int
    weight_kg: float
    lenght: float
    width: float
    height: float

    @property
    def volumetric_weight(self) -> float:
        return (self.lenght * self.width * self.height) / 6000

    @property
    def chargable_weight(self) -> float:
        return max(self.weight_kg, self.volumetric_weight)


@dataclass
class CostBreakdown:
    shipping_cost: float
    service_fee: float = 0.0
    oversize_fee: float = 0.0
    overweight_fee: float = 0.0
    
    @property
    def total_cost(self) -> float:
        return (self.shipping_cost + self.service_fee + 
                self.oversize_fee + self.overweight_fee)


@dataclass
class Quote:
    shipping_channel: str
    total_cost: float
    cost_breakdown: CostBreakdown
    shipping_time_range: dict