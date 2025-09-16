"""
Stock Processing Logic
----------------------
Core functions for evaluating and processing stock data.
"""

from .models import ProductList
from .utils import safe_float, normalize_quantity

def process_stock(product_list: ProductList) -> tuple[float, list[str]]:
    """
    Process stock data to calculate total stock value and out-of-stock items.

    Args:
        product_list (ProductList):
            List of products (Product ID, Price, Stock Quantity).

    Returns:
        Tuple[float, List[str]]:
            - Total stock value across all products.
            - List of product IDs that are out of stock.
    """
    total_value: float = 0.0
    out_of_stock_items: List[str] = []

    for product_id, price, quantity in product_list:
        price_value = safe_float(price)
        valid_quantity = normalize_quantity(quantity)

        stock_value = price_value * valid_quantity
        total_value += stock_value

        if valid_quantity == 0:
            out_of_stock_items.append(product_id)

    return total_value, out_of_stock_items
