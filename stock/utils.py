"""
Utility Functions for Stock Module
----------------------------------
Reusable helpers for validation, conversion, and safe data handling.
"""


def safe_float(value: float | str) -> float:
    """
    Safely convert a value to float.

    Args:
        value (float | str): The input value.

    Returns:
        float: Converted float, or 0.0 if conversion fails.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def normalize_quantity(quantity: int) -> int:
    """
    Ensure stock quantity is non-negative.

    Args:
        quantity (int): Original stock quantity.

    Returns:
        int: Quantity adjusted to be >= 0.
    """
    return max(quantity, 0)
