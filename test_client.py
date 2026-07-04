from bot.client import BinanceClient

client = BinanceClient()

balance = client.get_balance()

print(balance)