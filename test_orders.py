from bot.orders import OrderManager

manager = OrderManager()

balance = manager.get_balance()

print(balance)