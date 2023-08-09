from flask import request, jsonify
from dataclasses import asdict

from quote_api import app
from quote_api.models import Box
from quote_api.db_service import get_shipping_routes
from quote_api.utils import get_quote, setup_database

@app.route('/v1/quotes', methods=['POST'])
def get_shipping_quotes():
    request_data = request.json
    starting_country = request_data.get('starting_country')
    destination_country = request_data.get('destination_country')
    boxes_data = request_data.get('boxes', [])

    try:
        boxes = [Box(**box_data) for box_data in boxes_data]
    except (TypeError, SyntaxError):
        return jsonify('Bad request'), 400

    routes = get_shipping_routes(starting_country, destination_country)
    if not routes:
        return jsonify('Shipping route not available'), 400

    quotes = [get_quote(route, boxes) for route in routes]

    response = {'quotes': [asdict(quote) for quote in quotes if quote]}

    return jsonify(response), 200

@app.route('/', methods=['GET'])
def is_running():
    return jsonify('running'), 200

@app.route('/setup_database', methods=['GET'])
def initialize_database():
    setup_database()
    return jsonify('db created'), 200