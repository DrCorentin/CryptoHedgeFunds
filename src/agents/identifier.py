# File: src/agents/identifier.py

import pandas as pd

class CryptoIdentifier:
    def __init__(self, api_client):
        """
        Initialize the Crypto Identifier agent with a given API client.

        :param api_client: An object to interact with the Binance API.
        """
        self.api_client = api_client

    def identify_high_potential_cryptos(self):
        """
        Identifies high-potential cryptocurrencies based on trading volume, bid/ask spread, and liquidity.

        :return: A DataFrame of identified high-potential cryptos.
        """
        market_data = self.fetch_market_data()

        # Filter for liquid cryptos (e.g., volume > 1M)
        market_data['volume'] = pd.to_numeric(market_data['volume'], errors='coerce')
        market_data = market_data.dropna(subset=['volume'])
        liquid_cryptos = market_data[market_data['volume'] > 1_000_000]

        # Safely modify DataFrame
        liquid_cryptos = liquid_cryptos.copy()
        liquid_cryptos.loc[:, 'spread'] = (
            (liquid_cryptos['askPrice'] - liquid_cryptos['bidPrice']) / liquid_cryptos['askPrice']
        ) * 100

        # Sort by volume and smallest bid/ask spread
        liquid_cryptos = liquid_cryptos.sort_values(by=['volume', 'spread'], ascending=[False, True])

        return liquid_cryptos.head(10)

    def fetch_market_data(self):
        """
        Fetches market data from the Binance API.

        :return: A DataFrame containing market data.
        """
        tickers = self.api_client.client.get_ticker()
        data = []
        for ticker in tickers:
            data.append({
                'symbol': ticker['symbol'],
                'volume': ticker['volume'],
                'bidPrice': float(ticker['bidPrice']),
                'askPrice': float(ticker['askPrice']),
            })
        return pd.DataFrame(data)
