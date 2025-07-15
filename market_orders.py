import sys
from binance.client import Client
import logging
from datetime import datetime

# Binance API keys (Replace with your actual keys or use testnet)
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

client = Client(api_key, api_secret, testnet=True)

# Logging setup
logging.basicConfig(filename="bot.log", level=logging.INFO)

def log_order(action, symbol, quantity, status):
    logging.info(f"{datetime.now()} | {action} | {symbol} | qty: {quantity} | status: {status}")

symbol = sys.argv[1]
side = sys.argv[2].upper()
quantity = float(sys.argv[3])

try:
    order = client.futures_create_order(symbol=symbol, side=side, type='MARKET', quantity=quantity)
    log_order(side, symbol, quantity, "success")
    print("Market Order Placed:", order)
except Exception as e:
    log_order(side, symbol, quantity, f"error: {e}")
    print("Error:", e)
