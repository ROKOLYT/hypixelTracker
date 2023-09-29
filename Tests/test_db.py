import sys
import os

# Add the directory containing ocr.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_manager import fetch_data, plot_graph, clean_tests

def test_fetching_data():
    item = "TARANTULA_WEB"
    
    res = fetch_data(item)
    assert isinstance(res, list)
    
def test_plot():
    item = "TARANTULA_WEB"
    
    res = plot_graph(item)
    assert res is True
    
def clean_after_tests():
    res = clean_tests()
    
    assert res is True
        