import pandas as pd
from tools.api import get_market_data, get_social_data

class CryptoIdentifier:
    def __init__(self, top_n=10):
        self.top_n = top_n

    def identify_high_potential_cryptos(self):
        market_data = get_market_data()
        social_data = get_social_data()

        # Filter liquid crypto pairs
        liquid_cryptos = market_data[(market_data['volume'] > 1_000_000)]

        # Merge with social data
        combined_data = pd.merge(liquid_cryptos, social_data, on='symbol')

        # Scoring based on volume, bid/ask spread, and community activity
        combined_data['score'] = (
            combined_data['volume'] * 0.4 +
            (combined_data['bid_volume'] - combined_data['ask_volume']) * 0.3 +
            combined_data['community_activity'] * 0.3
        )

        # Select top N cryptos
        top_cryptos = combined_data.nlargest(self.top_n, 'score')
        return top_cryptos[['symbol', 'score']]

if __name__ == "__main__":
    identifier = CryptoIdentifier()
    top_cryptos = identifier.identify_high_potential_cryptos()
    print(top_cryptos)
