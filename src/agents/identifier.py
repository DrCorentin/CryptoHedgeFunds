class IdentifierAgent:
    def identify(self, market_data):
        # Check if 'price_change_percent' exists; fallback to a default value or compute it
        try:
            sorted_data = sorted(
                market_data.items(),
                key=lambda x: x[1].get('price_change_percent', 0),  # Default to 0 if key is missing
                reverse=True
            )
        except Exception as e:
            print("Error processing market data:", e)
            return []

        top_cryptos = [crypto[0] for crypto in sorted_data[:10]]
        return top_cryptos
