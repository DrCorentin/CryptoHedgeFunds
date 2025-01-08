# File: src/main.py

import os
import pandas as pd
from backtester import Backtester
from agents.identifier import CryptoIdentifier
from agents.portfolio_manager import PortfolioManager
from tools.api import BinanceAPI
from models.trading_model import TradingModel

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

    # Save recommendations to CSV
    save_recommendations(recommendations)

    # Step 3: Backtesting
    print("Starting Backtest...")
    historical_data = load_historical_data()  # Load historical data
    trading_model = TradingModel()  # Initialize TradingModel
    backtester = Backtester(model=trading_model, historical_data=historical_data)
    backtester.run_backtest()
    backtester.report()

def save_recommendations(recommendations):
    """
    Save recommendations to a CSV file.

    :param recommendations: DataFrame of trading recommendations.
    """
    output_dir = "data/recommendations/"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, "recommendations.csv")

    # Append or create the recommendations CSV
    if os.path.exists(filename):
        existing_data = pd.read_csv(filename)
        updated_data = pd.concat([existing_data, recommendations], ignore_index=True)
    else:
        updated_data = recommendations

    updated_data.to_csv(filename, index=False)
    print(f"Recommendations saved to {filename}")

def load_historical_data():
    """
    Load historical data for backtesting.
    Replace with actual data loading logic.

    :return: List of historical data points.
    """
    return [
        {"actual_signal": "buy", "price_change": 1.5},  # Example data point
        {"actual_signal": "hold", "price_change": 0.0},
        {"actual_signal": "sell", "price_change": -1.0},
        {"actual_signal": "buy", "price_change": 2.0},
    ]

if __name__ == "__main__":
    main()
