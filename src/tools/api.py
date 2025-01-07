import requests

class BinanceAPI:
    BASE_URL = "https://api.binance.com/api/v3/"

    def get_ticker(self, symbol):
        response = requests.get(f"{self.BASE_URL}ticker/24hr", params={"symbol": symbol})
        return response.json()

    def get_market_data(self):
        # Fetch all market data
        response = requests.get(f"{self.BASE_URL}exchangeInfo")
        return response.json()

class PancakeSwapAPI:
    # Add PancakeSwap-specific methods
    pass

def get_market_data():
    api = BinanceAPI()
    return api.get_market_data()
