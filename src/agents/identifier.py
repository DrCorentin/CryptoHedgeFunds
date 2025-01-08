from binance.client import Client
import pandas as pd

class CryptoIdentifier:
    def __init__(self, api_key=None, api_secret=None):
        # Initialize Binance API client
        self.client = Client(api_key, api_secret)

    def fetch_market_data(self):
        """
        Fetch market data from Binance and return a DataFrame.
        """
        # Fetch 24hr ticker price change statistics for all symbols
        tickers = self.client.get_ticker()

        # Extract relevant data into a DataFrame
        data = []
        for ticker in tickers:
            data.append({
                'symbol': ticker['symbol'],
                'volume': float(ticker['volume']),
                'price_change_percent': float(ticker['priceChangePercent']),
            })

        market_data = pd.DataFrame(data)
        return market_data

    def identify_high_potential_cryptos(self):
        # Fetch market data
        market_data = self.fetch_market_data()

        # Filter for high-volume cryptos
        market_data['volume'] = pd.to_numeric(market_data['volume'], errors='coerce')
        market_data = market_data.dropna(subset=['volume'])
        liquid_cryptos = market_data[market_data['volume'] > 1_000_000]

        # Sort by price change percentage (descending) to find high-potential cryptos
        liquid_cryptos = liquid_cryptos.sort_values(by='price_change_percent', ascending=False)

        # Return the top cryptos
        return liquid_cryptos

# Example usage
if __name__ == "__main__":
    identifier = CryptoIdentifier()  # Provide API keys if needed
    top_cryptos = identifier.identify_high_potential_cryptos()

    print("Top Cryptos Identified:")
    print(top_cryptos.head(10))  # Display the top 10 cryptos
