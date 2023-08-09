
def test_quotes_api_china(client, boxes):
    path = 'v1/quotes'
    response = client.post(path, json={
        'starting_country': 'China',
        'destination_country': 'USA',
        'boxes': boxes
    })
    assert response.get_json() == {
        "quotes": [
            {
                "cost_breakdown": {
                    "oversize_fee": 0.0,
                    "overweight_fee": 0.0,
                    "service_fee": 300,
                    "shipping_cost": 934.5
                },
                "shipping_channel": "air",
                "shipping_time_range": {
                    "max_days": 20,
                    "min_days": 15
                },
                "total_cost": 1234.5
            },
            {
                "cost_breakdown": {
                    "oversize_fee": 0.0,
                    "overweight_fee": 0.0,
                    "service_fee": 300,
                    "shipping_cost": 267.0
                },
                "shipping_channel": "ocean",
                "shipping_time_range": {
                    "max_days": 50,
                    "min_days": 45
                },
                "total_cost": 567.0
            }
        ]
    }

def test_quotes_api_india(client, boxes):
    path = 'v1/quotes'
    response = client.post(path, json={
        'starting_country': 'India',
        'destination_country': 'USA',
        'boxes': boxes
    })
    assert response.get_json() == {
        "quotes": [
            {
                "cost_breakdown": {
                    "oversize_fee": 0.0,
                    "overweight_fee": 800.0,
                    "service_fee": 0,
                    "shipping_cost": 1602.0
                },
                "shipping_channel": "air",
                "shipping_time_range": {
                    "max_days": 15,
                    "min_days": 10
                },
                "total_cost": 2402.0
            },
            {
                "cost_breakdown": {
                    "oversize_fee": 0.0,
                    "overweight_fee": 800.0,
                    "service_fee": 0,
                    "shipping_cost": 400.5
                },
                "shipping_channel": "ocean",
                "shipping_time_range": {
                    "max_days": 50,
                    "min_days": 40
                },
                "total_cost": 1200.5
            }
        ]
    }