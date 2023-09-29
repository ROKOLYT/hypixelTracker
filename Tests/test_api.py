import sys
import os

# Add the directory containing ocr.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api import bazaar_api

def test_api():
    api = bazaar_api()
    res = api.update_data()
    assert res is True
    
def test_data_insertion():
    api = bazaar_api()
    dummy = {
    "productId": {
        "sell_summary": [],
        "buy_summary": [],
        "quick_status": {
            "productId": "Dummy",
            "sellPrice": 0.0,
            "sellVolume": 0,
            "sellMovingWeek": 0,
            "sellOrders": 0,
            "buyPrice": 0.0,
            "buyVolume": 0,
            "buyMovingWeek": 0,
            "buyOrders": 0
            }
        }
    }
    res = api.update_data_base(dummy)
    assert res is None
        