import requests

class APIClient:
    BASE_URL = "https://api.binance.com/api/v3"

    def fetch_market_data(self):
        response = requests.get(f"{self.BASE_URL}/ticker/24hr")
        return response.json() if response.status_code == 200 else []
