import pandas as pd

class Backtester:
    def simulate(self, trades):
        # Simulate trading performance and save results to CSV
        results = []
        for trade in trades:
            result = {
                "timestamp": trade["timestamp"],
                "from_to": trade["from_to"],
                "price": trade["price"],
                "return_euro": trade["return_euro"],
                "return_btc": trade["return_btc"],
                "return_percentage": trade["return_percentage"]
            }
            results.append(result)

        df = pd.DataFrame(results)
        df.to_csv("data/logs/simulation_results.csv", index=False)
