import csv
import time

class Backtester:
    def __init__(self, starting_balance=50):
        self.starting_balance = starting_balance
        self.balance_eur = starting_balance
        self.balance_btc = 0
        self.portfolio = []
        self.trades = []

    def calculate_trade_amount(self, crypto):
        # Example logic: invest 10% of current EUR balance in each selected crypto
        trade_amount = self.balance_eur * 0.10  # 10% of the balance
        if trade_amount <= 0:
            print("Not enough EUR balance to execute trade.")
        return trade_amount

    def simulate_trade(self, from_currency, to_currency, amount, price):
        trade_value = amount * price
        if from_currency == 'EUR' and self.balance_eur >= trade_value:
            self.balance_eur -= trade_value
            self.portfolio.append({'currency': to_currency, 'amount': amount, 'price': price})
        elif from_currency == 'BTC' and self.balance_btc >= trade_value / price:
            self.balance_btc -= trade_value / price
            self.portfolio.append({'currency': to_currency, 'amount': amount, 'price': price})
        else:
            print(f"Insufficient funds to execute trade from {from_currency} to {to_currency}.")

        self.trades.append({
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount,
            'price': price,
        })

    def calculate_portfolio_value(self):
        total_eur = self.balance_eur
        for asset in self.portfolio:
            total_eur += asset['amount'] * asset['price']  # Value of crypto assets in EUR
        return total_eur

    def save_results(self):
        # Ensure there are trades before attempting to save results
        if not self.trades:
            print("No trades were made, skipping results saving.")
            return

        with open("data/logs/simulation_results.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.trades[0].keys())
            writer.writeheader()
            writer.writerows(self.trades)

        total_eur = self.calculate_portfolio_value()  # Total portfolio value in EUR
        with open("data/logs/portfolio_summary.csv", "w") as f:
            f.write(f"Final Portfolio Value (EUR): {total_eur}\n")
            f.write(f"Initial Balance (EUR): {self.starting_balance}\n")
            f.write(f"Total Return (EUR): {total_eur - self.starting_balance}\n")
            f.write(f"Total Return (%): {((total_eur / self.starting_balance) - 1) * 100:.2f}%\n")
            print("Portfolio summary saved.")

