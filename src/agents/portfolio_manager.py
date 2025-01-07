class PortfolioManager:
    def __init__(self):
        self.start_balance_euro = 50.0  # Starting balance in EUR
        self.current_balance_euro = 50.0
        self.current_balance_btc = 0.0  # BTC equivalent of the portfolio

    def combine_signals(self, *signals):
        # Average signals to make a unified decision
        average_score = sum(signal['score'] for signal in signals) / len(signals)
        return {"crypto": signals[0]["crypto"], "score": average_score}

    def allocate(self, combined_signals):
        # Allocate portfolio based on scores
        sorted_signals = sorted(combined_signals, key=lambda x: x["score"], reverse=True)
        portfolio = {signal["crypto"]: signal["score"] for signal in sorted_signals[:5]}
        return portfolio

    def generate_trades(self, portfolio):
        # AI-based trade generation
        trades = []
        for crypto, allocation in portfolio.items():
            amount = allocation * self.current_balance_euro  # Allocate portion of balance
            trades.append({
                'from': 'EUR',
                'to': crypto,
                'amount': amount
            })
        return trades

    def update_balances(self, trade_result):
        # Update balances based on trade results
        self.current_balance_euro = trade_result["return_euro"]
        self.current_balance_btc = trade_result["return_btc"]
