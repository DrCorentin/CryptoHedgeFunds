from binance.client import Client
import requests

# Binance Public Client
binance_client = Client(api_key=None, api_secret=None)

def get_binance_ticker(symbol: str):
    """
    Get the latest price ticker for a given symbol from Binance public API.
    """
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

#        ticker = binance_client.get_symbol_ticker(symbol=symbol)
#        return ticker

    except Exception as e:
        print(f"Error fetching Binance ticker for {symbol}: {e}")
        return None

def get_pancakeswap_prices():
    """
    Fetch token prices from PancakeSwap public API.
    Example: PancakeSwap doesn't have an official public API; use external APIs or smart contracts.
    """
    try:
        url = "https://api.pancakeswap.info/api/v2/tokens"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Error fetching PancakeSwap prices: {e}")
        return None
