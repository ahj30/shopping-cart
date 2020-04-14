import pytest
from datetime import datetime

from shopping_cart import to_usd, TAX_RATE, find_product, human_friendly_timestamp, calculate_tax, calculate_subtotal

def test_tax_rate():
    assert TAX_RATE == .0875

def test_calculate_tax():
    assert calculate_tax(100) == 8.75

def test_calculate_subtotal():
    #total of list working from subtotal lists valid
    example_list = [10,5,2,3,4]
    assert calculate_subtotal(example_list) == 24 

def test_to_usd():
    # it should apply USD formatting
    assert to_usd(4.50) == "$4.50"
    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"
    # it should round to two places
    assert to_usd(4.55555) == "$4.56"
    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_find_product():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]
    # if there is a match, it should find and return a product
    matching_product = find_product("1", products)
    assert matching_product["name"] == "Chocolate Sandwich Cookies"
    matching_product = find_product("2", products)
    assert matching_product["name"] == "All-Seasons Salt"
    matching_product = find_product("3", products)
    assert matching_product["name"] == "Robust Golden Unsweetened Oolong Tea"
    # if there is no match, it should raise an IndexError
    with pytest.raises(IndexError):
        find_product("2222", products)

def test_human_friendly_timestamp():
    # check for 12 hour scale and PM time
    test_date = datetime(2020, 4, 1, 16, 31, 16)
    assert human_friendly_timestamp(test_date) == "2020-04-01 04:31:16 PM"
    # check for AM time
    testtwo_date =datetime (2020, 12, 27, 3, 18, 22)
    assert human_friendly_timestamp(testtwo_date) == "2020-12-27 03:18:22 AM"




