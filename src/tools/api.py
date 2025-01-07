import requests

def get_binance_prices():
    """
    Fetches market data from Binance.
    """
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)

    # Check for HTTP errors
    if response.status_code != 200:
        raise ConnectionError(f"Failed to fetch Binance data: {response.status_code} {response.reason}")

    data = response.json()
    market_data = {}

    for item in data:
        market_data[item['symbol']] = {
            'price': float(item['lastPrice']),
            'price_change_percent': float(item['priceChangePercent'])
        }
    return market_data


def get_market_data():
    try:
        response = requests.get("https://api.binance.com/api/v3/ticker/24hr")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching market data: {e}")
        return {}
