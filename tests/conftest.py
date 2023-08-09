import pytest
from pytest import Session

from quote_api import app
from quote_api.models import Box
from quote_api.utils import read_rates_file

@pytest.fixture
def boxes():
    """
    total chargeable weight: 267
    for India: 800 in overweight fees
    for Vietnam: 600 in oversized fees
    """
    return [
        Box(count=3,weight_kg=14,lenght=50,width=40,height=25), 
        Box(count=4,weight_kg=25,lenght=45,width=65,height=20),
        Box(count=6,weight_kg=20,lenght=50,width=100,height=25)
    ]

@pytest.fixture
def routes():
    return read_rates_file('aux_files/rates.json')

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            yield client