import pandas as pd
import requests

def get_market_data():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df[['symbol', 'volume', 'bidPrice', 'askPrice', 'bidQty', 'askQty']]
    else:
        raise Exception("Error fetching market data")

def get_social_data():
    # Placeholder: Simulate community activity score
    # Extend with real API calls to social media analytics
    symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
    activity_scores = {symbol: 100 for symbol in symbols}  # Mock data
    return pd.DataFrame(list(activity_scores.items()), columns=['symbol', 'community_activity'])


