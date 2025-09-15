"""
Main Runner Script
------------------
Runs the stock processing module with sample data.
"""

from stock.data import products
from stock.processor import process_stock


def main() -> None:
    """Run stock analysis with demo dataset."""
    stock_value, low_stock = process_stock(products)
    print(f"Total value of all stock: {stock_value:.2f}")
    print(f"Out of stock products: {low_stock}")


if __name__ == "__main__":
    main()
