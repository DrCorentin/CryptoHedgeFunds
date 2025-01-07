class IdentifierAgent:
    def identify(self, market_data):
        # Safely access 'price_change_percent' with a default value
        try:
            sorted_data = sorted(
                market_data.items(),
                key=lambda x: float(x[1].get('price_change_percent', 0)),  # Default to 0 if missing
                reverse=True
            )
        except Exception as e:
            print("Error sorting market data:", e)
            return []

        top_cryptos = [crypto[0] for crypto in sorted_data[:10]]
        return top_cryptos
