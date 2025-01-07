class IdentifierAgent:
    def identify(self, market_data):
        # Identify top 10 high-potential cryptos based on basic volume and price changes
        sorted_data = sorted(market_data.items(), key=lambda x: x[1]['price_change_percent'], reverse=True)
        return [crypto[0] for crypto in sorted_data[:10]]
