# File: src/main.py

import os
import pandas as pd
from agents.identifier import CryptoIdentifier
from agents.portfolio_manager import PortfolioManager
from tools.api import BinanceAPI

def main():
    # Initialize API client (using public API for learning model)
    binance_api = BinanceAPI()

    # Step 1: Identify potential cryptos
    identifier = CryptoIdentifier(api_client=binance_api)
    top_cryptos = identifier.identify_high_potential_cryptos()

    print("Top Cryptos Identified:")
    print(top_cryptos)

    # Step 2: Portfolio management and recommendation generation
    portfolio_manager = PortfolioManager(api_client=binance_api)
    recommendations = portfolio_manager.generate_recommendations(top_cryptos)

    # Step 3: Save recommendations to CSV
    save_recommendations(recommendations)

def save_recommendations(recommendations):
    output_dir = "data/recommendations/"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, "recommendations.csv")

    # Append or create the recommendations CSV
    if os.path.exists(filename):
        existing_data = pd.read_csv(filename)
        updated_data = pd.concat([existing_data, recommendations])
    else:
        updated_data = recommendations

    updated_data.to_csv(filename, index=False)
    print(f"Recommendations saved to {filename}")

if __name__ == "__main__":
    main()
