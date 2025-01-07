import pandas as pd
from tools.api import get_binance_prices
import time

class Backtester:
    def __init__(self):
        self.start_balance_euro = 1000  # Initial fund balance in EUR
        self.start_balance_btc = 0.05  # Initial fund balance in BTC
        self.start_date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        self.trades = []

    def simulate_trade(self, from_asset, to_asset, amount):
        """
        Simulate a trade using public market prices.
        """
        if to_asset == "BTC":
            ticker = get_binance_prices("BTCUSDT")
            price = float(get_binance_prices["price"]) if ticker else None
        elif to_asset == "ETH":
            ticker = get_binance_prices("ETHUSDT")
            price = float(ticker["price"]) if ticker else None
        else:
            prices = get_pancakeswap_prices()
            price = (
                float(prices["data"].get(to_asset, {}).get("price", 0))
                if prices else None
            )

        if not price:
            print(f"Error: Could not fetch price for {to_asset}. Trade skipped.")
            return

        return_euro = amount * price if from_asset == "EUR" else amount / price
        return_btc = return_euro / price
        return_percentage = (return_euro / self.start_balance_euro - 1) * 100

        trade = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
            "from_to": f"{from_asset} -> {to_asset}",
            "price": price,
            "return_euro": return_euro,
            "return_btc": return_btc,
            "return_percentage": return_percentage,
        }
        self.trades.append(trade)
        print(f"Trade executed: {trade}")

    def save_results(self):
        """
        Save all trades to a CSV file.
        """
        df = pd.DataFrame(self.trades)
        df.to_csv("data/logs/simulation_results.csv", index=False)
        print("Simulation results saved to data/logs/simulation_results.csv")

if __name__ == "__main__":
    backtester = Backtester()
    backtester.simulate_trade("EUR", "BTC", 500)
    backtester.simulate_trade("BTC", "ETH", 0.01)
    backtester.save_results()
