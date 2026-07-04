"""
Input validation utilities.
"""

from typing import Optional


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol.
    """
    symbol = symbol.upper().strip()

    if len(symbol) < 6:
        raise ValueError("Invalid trading symbol.")

    return symbol


def validate_side(side: str) -> str:
    """
    Validate BUY/SELL.
    """
    side = side.upper().strip()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate MARKET/LIMIT.
    """
    order_type = order_type.upper().strip()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate quantity.
    """
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price: Optional[float], order_type: str) -> Optional[float]:
    """
    Validate limit order price.
    """
    if order_type == "LIMIT":

        if price is None:
            raise ValueError("LIMIT order requires a price.")

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

    return price