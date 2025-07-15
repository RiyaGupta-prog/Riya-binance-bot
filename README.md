# Binance Futures Trading Bot - Riya

## 🔧 Setup
1. Install required package:
```bash
pip install python-binance
```

2. Replace API Key & Secret in the scripts:
```python
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
```

3. Run Example Commands:
```bash
python market_orders.py BTCUSDT BUY 0.01
python limit_orders.py BTCUSDT SELL 0.01 58000
python advanced/stop_limit.py BTCUSDT SELL 0.01 58200 58000
```

## 🧠 Features
- Market & Limit Orders
- Stop-Limit (simulated)
- OCO, TWAP, Grid (basic structure)
- Logging all actions to bot.log

## 📁 Folder Structure
```
src/
├── market_orders.py
├── limit_orders.py
└── advanced/
    ├── stop_limit.py
    ├── oco.py
    ├── twap.py
    └── grid_orders.py
```
