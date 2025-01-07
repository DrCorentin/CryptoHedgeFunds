class Backtester:
    def __init__(self):
        self.trades = []
        self.total_performance = {"EUR": 50.0, "BTC": 0.0}  # Initial portfolio value

    def simulate_trade(self, from_asset, to_asset, amount):
        # Simulate trade using real market data
        price = self.get_price(to_asset)
        if not price:
            print(f"Error: Could not fetch price for {to_asset}. Trade skipped.")
            return

        return_euro = amount * price if from_asset == "EUR" else amount / price
        return_btc = return_euro / price

        trade = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
            "from_to": f"{from_asset} -> {to_asset}",
            "price": price,
            "return_euro": return_euro,
            "return_btc": return_btc,
        }

        # Update performance
        self.total_performance["EUR"] = trade["return_euro"]
        self.total_performance["BTC"] = trade["return_btc"]
        self.trades.append(trade)
        print(f"Trade executed: {trade}")

    def get_price(self, to_asset):
        # Simulate price fetching from Binance or other APIs
        prices = get_binance_prices()
        return float(prices.get(to_asset, {}).get("price", 0))


def save_results(self):
        # Ensure the directory exists
        logs_dir = "data/logs"
        os.makedirs(logs_dir, exist_ok=True)

        # Save results to a file
        with open(f"{logs_dir}/simulation_results.csv", "w") as f:
            f.write("timestamp,from_to,price,return_euro,return_btc,return_percentage\n")
            for trade in self.trades:
                f.write(f"{trade['timestamp']},{trade['from_to']},{trade['price']},{trade['return_euro']},{trade['return_btc']},{trade['return_percentage']}\n")
        print(f"Simulation results saved to {logs_dir}/simulation_results.csv")
