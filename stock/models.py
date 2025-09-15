"""
Data Models for Stock Module
----------------------------
Defines the core types and data structures used in the stock system.
"""

from typing import Tuple, List, Union

Product = Tuple[str, Union[float, str], int]
ProductList = List[Product]
