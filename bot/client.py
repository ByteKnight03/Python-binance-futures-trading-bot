"""
Binance Futures Testnet REST API Client.
"""

import hashlib
import hmac
import time

import requests

from bot.config import settings
from bot.exceptions import BinanceAPIError
from bot.logging_config import setup_logger

logger = setup_logger()


class BinanceClient:
    """Client for interacting with Binance Futures Testnet."""

    def __init__(self):
        self.api_key = settings.api_key
        self.api_secret = settings.api_secret
        self.base_url = settings.base_url

    def _headers(self):
        return {
            "X-MBX-APIKEY": self.api_key
        }

    def _generate_signature(self, query_string: str) -> str:
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

    def _request(self, method: str, endpoint: str, params=None):
        """Send signed request."""

        if params is None:
            params = {}

        params["timestamp"] = int(time.time() * 1000)

        # IMPORTANT: Keep original insertion order
        query_string = "&".join(
            f"{key}={value}" for key, value in params.items()
        )

        params["signature"] = self._generate_signature(query_string)

        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self._headers(),
                params=params,
                timeout=10,
            )

            if response.status_code != 200:
                try:
                    error = response.json()
                    logger.error(error)
                    raise BinanceAPIError(
                        f"{error.get('code')} : {error.get('msg')}"
                    )
                except Exception:
                    raise BinanceAPIError(response.text)

            return response.json()

        except requests.exceptions.RequestException as e:
            logger.error(str(e))
            raise BinanceAPIError(str(e))

    # =====================================================
    # ACCOUNT
    # =====================================================

    def get_balance(self):
        return self._request(
            "GET",
            "/fapi/v2/balance",
        )

    def get_account_info(self):
        return self._request(
            "GET",
            "/fapi/v2/account",
        )

    # =====================================================
    # MARKET DATA
    # =====================================================

    def get_price(self, symbol: str):
        response = requests.get(
            f"{self.base_url}/fapi/v1/ticker/price",
            params={
                "symbol": symbol.upper()
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    # =====================================================
    # ORDERS
    # =====================================================

    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
    ):

        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": "MARKET",
            "quantity": quantity,
        }

        return self._request(
            "POST",
            "/fapi/v1/order",
            params,
        )

    def get_order(
        self,
        symbol: str,
        order_id: int,
    ):

        params = {
            "symbol": symbol.upper(),
            "orderId": order_id,
        }

        return self._request(
            "GET",
            "/fapi/v1/order",
            params,
        )

    def cancel_order(
        self,
        symbol: str,
        order_id: int,
    ):

        params = {
            "symbol": symbol.upper(),
            "orderId": order_id,
        }

        return self._request(
            "DELETE",
            "/fapi/v1/order",
            params,
        )

    def get_open_orders(self, symbol=None):

        params = {}

        if symbol:
            params["symbol"] = symbol.upper()

        return self._request(
            "GET",
            "/fapi/v1/openOrders",
            params,
        )