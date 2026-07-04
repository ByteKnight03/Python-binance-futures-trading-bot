"""
Professional CLI for Binance Futures Testnet Trading Bot.
"""

import argparse

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from bot.orders import OrderManager

console = Console()
manager = OrderManager()


def show_balance():
    balances = manager.get_balance()

    table = Table(title="💰 Binance Futures Testnet Balance")

    table.add_column("Asset", style="cyan")
    table.add_column("Balance", style="green")
    table.add_column("Available", style="yellow")

    for asset in balances:
        if float(asset["balance"]) > 0:
            table.add_row(
                asset["asset"],
                asset["balance"],
                asset["availableBalance"],
            )

    console.print(table)


def show_summary():
    summary = manager.get_account_summary()

    table = Table(title="📊 Account Summary")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Wallet Balance", summary["wallet_balance"])
    table.add_row("Available Balance", summary["available_balance"])
    table.add_row("Margin Balance", summary["margin_balance"])
    table.add_row("Unrealized PnL", summary["unrealized_pnl"])

    console.print(table)

def show_account():
    """Display formatted account information."""

    account = manager.get_account_info()

    assets = account["assets"]

    usdt = next(
        asset for asset in assets
        if asset["asset"] == "USDT"
    )

    table = Table(title="📊 Binance Futures Account")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Wallet Balance", usdt["walletBalance"])
    table.add_row("Available Balance", usdt["availableBalance"])
    table.add_row("Margin Balance", usdt["marginBalance"])
    table.add_row("Unrealized PnL", usdt["unrealizedProfit"])
    table.add_row("Initial Margin", account["totalInitialMargin"])
    table.add_row("Open Order Margin", account["totalOpenOrderInitialMargin"])
    table.add_row("Maintenance Margin", account["totalMaintMargin"])

    console.print(table)

def show_price(symbol):
    price = manager.get_price(symbol)

    table = Table(title="📈 Live Price")

    table.add_column("Symbol", style="cyan")
    table.add_column("Price", style="green")

    table.add_row(
        price["symbol"],
        price["price"],
    )

    console.print(table)


def show_positions():

    positions = manager.get_positions()

    if not positions:
        console.print("[yellow]No open positions.[/yellow]")
        return

    table = Table(title="📌 Open Positions")

    table.add_column("Symbol")
    table.add_column("Side")
    table.add_column("Quantity")
    table.add_column("Entry Price")
    table.add_column("PnL")

    for pos in positions:

        side = "LONG"

        if float(pos["positionAmt"]) < 0:
            side = "SHORT"

        table.add_row(
            pos["symbol"],
            side,
            pos["positionAmt"],
            pos["entryPrice"],
            pos["unrealizedProfit"],
        )

    console.print(table)


def show_open_orders():

    orders = manager.get_open_orders()

    if not orders:
        console.print("[yellow]No open orders.[/yellow]")
        return

    table = Table(title="📋 Open Orders")

    table.add_column("Order ID")
    table.add_column("Symbol")
    table.add_column("Side")
    table.add_column("Quantity")
    table.add_column("Status")

    for order in orders:

        table.add_row(
            str(order["orderId"]),
            order["symbol"],
            order["side"],
            order["origQty"],
            order["status"],
        )

    console.print(table)


def show_order(result):

    text = Text()

    text.append(
        "✅ ORDER PLACED SUCCESSFULLY\n\n",
        style="bold green",
    )

    text.append(f"Order ID : {result['orderId']}\n")
    text.append(f"Symbol   : {result['symbol']}\n")
    text.append(f"Side     : {result['side']}\n")
    text.append(f"Quantity : {result['origQty']}\n")
    text.append(f"Status   : {result['status']}\n")
    text.append(f"Type     : {result['type']}")

    console.print(
        Panel(
            text,
            title="Order Confirmation",
            border_style="green",
        )
    )

def main():

    parser = argparse.ArgumentParser(
        description="Professional Binance Futures Testnet Trading Bot"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Balance
    subparsers.add_parser(
        "balance",
        help="Show account balance"
    )

    # Account
    subparsers.add_parser(
        "account",
        help="Show account information"
    )

    # Summary
    subparsers.add_parser(
        "summary",
        help="Show account summary"
    )

    # Price
    price = subparsers.add_parser(
        "price",
        help="Show live market price"
    )

    price.add_argument("symbol")

    # Positions
    subparsers.add_parser(
        "positions",
        help="Show open positions"
    )

    # Open Orders
    subparsers.add_parser(
        "open-orders",
        help="Show open orders"
    )

    # Buy
    buy = subparsers.add_parser(
        "buy",
        help="Place Market BUY order"
    )

    buy.add_argument("symbol")
    buy.add_argument("quantity", type=float)

    # Sell
    sell = subparsers.add_parser(
        "sell",
        help="Place Market SELL order"
    )

    sell.add_argument("symbol")
    sell.add_argument("quantity", type=float)

    # Order
    order = subparsers.add_parser(
        "order",
        help="Get order details"
    )

    order.add_argument("symbol")
    order.add_argument("order_id", type=int)

    # Cancel
    cancel = subparsers.add_parser(
        "cancel",
        help="Cancel an order"
    )

    cancel.add_argument("symbol")
    cancel.add_argument("order_id", type=int)

    args = parser.parse_args()


    try:

        if args.command == "balance":
            show_balance()

        elif args.command == "account":
            show_account()

        elif args.command == "summary":
            show_summary()

        elif args.command == "price":
            show_price(args.symbol)

        elif args.command == "positions":
            show_positions()

        elif args.command == "open-orders":
            show_open_orders()

        elif args.command == "buy":

            result = manager.buy_market(
                args.symbol,
                args.quantity,
            )

            show_order(result)

        elif args.command == "sell":

            result = manager.sell_market(
                args.symbol,
                args.quantity,
            )

            show_order(result)

        elif args.command == "order":

            result = manager.get_order(
                args.symbol,
                args.order_id,
            )

            console.print(
                Panel.fit(
                    str(result),
                    title="📄 Order Details",
                    border_style="cyan",
                )
            )

        elif args.command == "cancel":

            result = manager.cancel_order(
                args.symbol,
                args.order_id,
            )

            console.print(
                Panel.fit(
                    str(result),
                    title="❌ Order Cancelled",
                    border_style="red",
                )
            )

        else:
            parser.print_help()

    except Exception as e:
        console.print(
            Panel.fit(
                str(e),
                title="⚠ Error",
                border_style="red",
            )
        )


if __name__ == "__main__":
    main()