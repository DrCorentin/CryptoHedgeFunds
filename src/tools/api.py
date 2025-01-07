from binance.client import Client
import requests

# Binance Public Client
binance_client = Client(api_key=None, api_secret=None)

def get_binance_ticker():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()

    # Inspect sample data
    print("Binance Market Data Sample:", data[:5])

    # Ensure `price_change_percent` is present
    market_data = {}
    for ticker in data:
        market_data[ticker['symbol']] = {
            'price_change_percent': float(ticker.get('priceChangePercent', 0)),  # Use default 0 if missing
            'price': float(ticker['lastPrice']),
        }
    return market_data

def get_pancakeswap_prices():
    url = "https://api.pancakeswap.info/api/v2/tokens"
    response = requests.get(url)
    data = response.json()

    # Inspect sample data
    print("PancakeSwap Market Data Sample:", list(data['data'].items())[:5])

    market_data = {}
    for token, info in data['data'].items():
        market_data[token] = {
            'price': float(info.get('price', 0)),
            'price_change_percent': 0  # Replace with actual calculation if available
        }
    return market_data
