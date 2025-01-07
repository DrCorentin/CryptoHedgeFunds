class PortfolioManager:
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
        # Create buy/sell trades based on portfolio allocation
        trades = []
        for crypto, score in portfolio.items():
            trade = {
                "crypto": crypto,
                "action": "buy",  # For simplicity, we assume all trades are 'buy' for now
                "amount": score  # This could be adjusted to reflect the asset size
            }
            trades.append(trade)
        return trades
