class IdentifierAgent:
    def identify(self, market_data):
        # Process market data to identify top 10 cryptos with high growth potential
        high_potential_cryptos = sorted(
            market_data, key=lambda x: x['growth_potential'], reverse=True
        )[:10]
        return high_potential_cryptos
