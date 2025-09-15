"""
Sample Product Dataset
----------------------
This dataset is for demonstration purposes.
"""

from .models import ProductList

products: ProductList = [
    ("p001", 150.00, 5),
    ("p002", 200.00, 0),
    ("p003", 50.50, 10),
    ("p004", "99.99", 3),   # Price as string
    ("p005", 300.00, 0),
    ("p006", 75.00, -1),    # Negative stock
]
