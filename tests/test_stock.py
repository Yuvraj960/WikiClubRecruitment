"""
Pytest Unit Tests for Stock Module
----------------------------------
Covers normal cases and edge cases:
1. Normal product list
2. Price as string
3. Invalid price
4. Negative quantity
5. Out of stock
"""

import pytest
from stock.processor import process_stock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_normal_case():
    """Products with valid float prices and positive quantities."""
    products = [("p001", 100.0, 2), ("p002", 50.0, 4)]
    total, out = process_stock(products)
    assert total == 100 * 2 + 50 * 4
    assert out == []


def test_string_price():
    """Price provided as a string should be converted correctly."""
    products = [("p003", "200.0", 1)]
    total, out = process_stock(products)
    assert total == 200.0
    assert out == []


def test_invalid_price():
    """Invalid price string should be treated as 0.0."""
    products = [("p004", "abc", 5)]
    total, out = process_stock(products)
    assert total == 0.0
    assert out == []


def test_negative_quantity():
    """Negative quantity should be treated as zero (out of stock)."""
    products = [("p005", 100.0, -3)]
    total, out = process_stock(products)
    assert total == 0.0
    assert out == ["p005"]


def test_out_of_stock():
    """Zero quantity should mark product as out of stock."""
    products = [("p006", 150.0, 0), ("p007", 50.0, 2)]
    total, out = process_stock(products)
    assert total == 50.0 * 2
    assert out == ["p006"]

def test_empty_product_list():
    """Empty product list should return zero value and empty out-of-stock list."""
    products = []
    total, out = process_stock(products)
    assert total == 0.0
    assert out == []


def test_zero_price():
    """Product with zero price should contribute nothing to total but not be out of stock if quantity > 0."""
    products = [("p008", 0.0, 5)]
    total, out = process_stock(products)
    assert total == 0.0
    assert out == []


def test_large_values():
    """Large price and quantity should not break calculation."""
    products = [("p009", 1e6, 1_000)]
    total, out = process_stock(products)
    assert total == 1e9  # 1 million * 1000
    assert out == []


def test_float_precision():
    """Ensure floating-point prices are handled correctly."""
    products = [("p013", 0.1, 3)]
    total, out = process_stock(products)
    assert abs(total - 0.3) < 1e-9
    assert out == []
