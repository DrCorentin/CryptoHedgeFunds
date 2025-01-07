import requests

def get_binance_ticker():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()

    market_data = {}
    for ticker in data:
        market_data[ticker['symbol']] = {
            'price_change_percent': float(ticker.get('priceChangePercent', 0)),  # Default to 0 if missing
            'price': float(ticker['lastPrice']),
        }
    return market_data


def get_pancakeswap_prices():
    url = "https://api.pancakeswap.info/api/v2/tokens"
    response = requests.get(url)
    data = response.json()

    market_data = {}
    for token, info in data['data'].items():
        market_data[token] = {
            'price': float(info.get('price', 0)),
            'price_change_percent': 0,  # Default or calculate if available
        }
    return market_data


def get_market_data():
    binance_data = get_binance_ticker()
    pancakeswap_data = get_pancakeswap_prices()

    # Merge the two data sources
    market_data = {**binance_data, **pancakeswap_data}
    return market_data
