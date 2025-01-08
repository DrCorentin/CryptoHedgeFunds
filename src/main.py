# File: src/main.py

import os
import pandas as pd
from backtester import Backtester
from agents.identifier import CryptoIdentifier
from agents.portfolio_manager import PortfolioManager
from tools.api import BinanceAPI

def main():
    # Initialize API client
    api_client = BinanceAPI()

    # Step 1: Identify high-potential cryptos
    identifier = CryptoIdentifier(api_client=api_client)
    high_potential_cryptos = identifier.identify_high_potential_cryptos()

    print("Top Cryptos Identified:")
    print(high_potential_cryptos)

    # Step 2: Portfolio management
    portfolio_manager = PortfolioManager(api_client=api_client)
    recommendations = portfolio_manager.generate_recommendations(high_potential_cryptos)

    print("Generated Recommendations:")
    print(recommendations)

    # Step 3: Backtesting
    print("Starting Backtest...")
    historical_data = load_historical_data()  # Load historical data
    backtester = Backtester(model=portfolio_manager, historical_data=historical_data)
    backtester.run_backtest()
    backtester.report()

def load_historical_data():
    # Replace with actual code to load historical data
    return [
        {"actual_signal": "buy", "price_change": 1.5},  # Example data point
        {"actual_signal": "hold", "price_change": 0.0},
        {"actual_signal": "sell", "price_change": -1.0},
        {"actual_signal": "buy", "price_change": 2.0},
    ]

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
