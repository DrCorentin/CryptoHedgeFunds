class FundamentalsAgent:
    def analyze_fundamentals(self, crypto_data):
        # Debugging: Print crypto_data to check its structure
#        print(f"Debug: crypto_data = {crypto_data}")

        # Use alternative metrics for analysis
        try:
            # Assume market cap is approximated using volume * last price
            volume = float(crypto_data.get('volume', 0))
            last_price = float(crypto_data.get('lastPrice', 0))
            market_cap_estimate = volume * last_price  # Estimated market cap
            
            print(f"Debug: Estimated market_cap = {market_cap_estimate}")
            return market_cap_estimate > 1_000_000_000  # Example threshold
        except ValueError:
            raise ValueError(f"Invalid data format: {crypto_data}")
