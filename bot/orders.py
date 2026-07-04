"""
Order management for Binance Futures Testnet.
"""

from bot.client import BinanceClient
from bot.validators import (
    validate_symbol,
    validate_quantity,
)

client = BinanceClient()


class OrderManager:
    """Handles all trading operations."""

    def buy_market(self, symbol: str, quantity: float):
        """Place a market BUY order."""

        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)

        return client.place_market_order(
            symbol=symbol,
            side="BUY",
            quantity=quantity,
        )

    def sell_market(self, symbol: str, quantity: float):
        """Place a market SELL order."""

        symbol = validate_symbol(symbol)
        quantity = validate_quantity(quantity)

        return client.place_market_order(
            symbol=symbol,
            side="SELL",
            quantity=quantity,
        )

    def cancel_order(self, symbol: str, order_id: int):
        """Cancel an order."""

        symbol = validate_symbol(symbol)

        return client.cancel_order(
            symbol=symbol,
            order_id=order_id,
        )

    def get_order(self, symbol: str, order_id: int):
        """Get details of an order."""

        symbol = validate_symbol(symbol)

        return client.get_order(
            symbol=symbol,
            order_id=order_id,
        )

    def get_balance(self):
        """Return account balances."""

        return client.get_balance()

    def get_account_info(self):
        """Return account information."""

        return client.get_account_info()

    def get_price(self, symbol: str):
        """Return the latest market price."""

        symbol = validate_symbol(symbol)

        return client.get_price(symbol)

    def get_positions(self):
        """
        Return only open positions.
        """

        account = client.get_account_info()

        positions = []

        for position in account.get("positions", []):

            if float(position["positionAmt"]) != 0:
                positions.append(position)

        return positions

    def get_open_orders(self, symbol: str = None):
        """
        Return open orders.
        """

        params = {}

        if symbol:
            params["symbol"] = validate_symbol(symbol)

        return client._request(
            "GET",
            "/fapi/v1/openOrders",
            params,
        )

    def get_account_summary(self):
        """
        Return a simplified account summary.
        """

        account = client.get_account_info()

        assets = account.get("assets", [])

        usdt = next(
            (
                asset
                for asset in assets
                if asset["asset"] == "USDT"
            ),
            None,
        )

        if usdt is None:
            return {}

        return {
            "wallet_balance": usdt["walletBalance"],
            "available_balance": usdt["availableBalance"],
            "margin_balance": usdt["marginBalance"],
            "unrealized_pnl": usdt["unrealizedProfit"],
        }