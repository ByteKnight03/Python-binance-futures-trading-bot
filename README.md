# 🚀 Binance Futures Testnet Trading Bot

A professional command-line trading bot built with **Python** for the **Binance Futures Testnet**. This project demonstrates secure API integration, REST API communication, object-oriented programming, input validation, logging, exception handling, and a user-friendly command-line interface.

---

## ✨ Features

- 🔐 Secure Binance API authentication using HMAC SHA256
- 💰 View Futures account balance
- 📊 View account summary
- 📈 Fetch live market prices
- 📌 View open positions
- 📋 View open orders
- 🟢 Place Market BUY orders
- 🔴 Place Market SELL orders
- ❌ Cancel existing orders
- 🔍 Fetch order details
- ✅ Input validation
- 📝 Logging support
- ⚠️ Custom exception handling
- 🎨 Rich CLI interface

---

## 📂 Project Structure

```text
trading-bot-binance/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── tests/
│   ├── test_client.py
│   ├── test_exceptions.py
│   ├── test_validators.py
│   └── ...
│
├── logs/
├── screenshots/
├── cli.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3
- Binance Futures Testnet REST API
- Requests
- Rich
- python-dotenv

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ByteKnight03/trading-bot-binance.git
cd trading-bot-binance
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

You can obtain your API keys from the Binance Futures Testnet.

---

## 💻 Usage

### Show Balance

```bash
py cli.py balance
```

### Show Account Information

```bash
py cli.py account
```

### Show Account Summary

```bash
py cli.py summary
```

### Get Live Price

```bash
py cli.py price BTCUSDT
```

### View Open Positions

```bash
py cli.py positions
```

### View Open Orders

```bash
py cli.py open-orders
```

### Place Market BUY Order

```bash
py cli.py buy BTCUSDT 0.001
```

### Place Market SELL Order

```bash
py cli.py sell BTCUSDT 0.001
```

### Get Order Details

```bash
py cli.py order BTCUSDT ORDER_ID
```

### Cancel an Order

```bash
py cli.py cancel BTCUSDT ORDER_ID
```

---

## 🧪 Testing

Run the test files individually:

```bash
py test_validators.py
```

```bash
py test_exceptions.py
```

```bash
py test_client.py
```

---

## 📸 Screenshots

### 💰 Account Balance
![Account Balance](screenshots/balance.png)

---

### 📊 Account Summary
![Account Summary](screenshots/summary.png)

---

### 📈 Live Price
![Live Price](screenshots/price.png)

---

### 🟢 Buy Order Confirmation
![Buy Order Confirmation](screenshots/buy.png)

---

### 📌 Open Positions
![Open Positions](screenshots/positions.png)

---

### 📋 Open Orders
![Open Orders](screenshots/open-orders.png)

---

### 👤 Account Details
![Account Details](screenshots/account.png)
---

## 📚 Learning Outcomes

This project demonstrates:

- REST API Integration
- Secure API Authentication (HMAC SHA256)
- Environment Variable Management
- Object-Oriented Programming
- Command-Line Interface Development
- Logging and Monitoring
- Exception Handling
- Input Validation
- Modular Software Design

---

## 🚀 Future Improvements

- Support for Limit Orders
- Stop-Loss and Take-Profit Orders
- Trade History
- Portfolio Analytics
- WebSocket Integration for Live Market Data
- Docker Support
- Automated Trading Strategies

---

## 👨‍💻 Author

**Shikhar Rastogi**

GitHub: https://github.com/ByteKnight03