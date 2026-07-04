"""
Application configuration.

Loads environment variables and stores application-wide constants.
"""

from dataclasses import dataclass
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Application settings."""

    api_key: str
    api_secret: str

    # Default Binance Futures endpoint.
    # We keep this in one place so it can easily be changed later.
    base_url: str = "https://testnet.binancefuture.com"


settings = Settings(
    api_key=os.getenv("BINANCE_API_KEY", ""),
    api_secret=os.getenv("BINANCE_API_SECRET", "")
)

if not settings.api_key or not settings.api_secret:
    raise ValueError(
        "Missing Binance API credentials. Please check your .env file."
    )