class ValuationAgent:
    def calculate_intrinsic_value(self, crypto_data):
        # Debugging: Print crypto_data to check its structure
        print(f"Debug: crypto_data = {crypto_data}")
        
        # Handle missing keys
        try:
            price = float(crypto_data.get('price', 0))  # Default to 0 if 'price' is missing
            volume = float(crypto_data.get('volume', 0))  # Default to 0 if 'volume' is missing
        except ValueError:
            raise ValueError(f"Invalid data format: {crypto_data}")

        # Calculate intrinsic value
        return price * 0.95 if volume > 1_000_000 else price
