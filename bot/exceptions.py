"""
Custom exceptions for the trading bot.
"""


class TradingBotError(Exception):
    """Base exception for the application."""
    pass


class ValidationError(TradingBotError):
    """Raised when user input is invalid."""
    pass


class BinanceAPIError(TradingBotError):
    """Raised when the Binance API returns an error."""
    pass


class NetworkError(TradingBotError):
    """Raised when a network issue occurs."""
    pass