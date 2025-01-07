class TechnicalsAgent:
    def analyze_technical_indicators(self, price_data):
        # Dummy example: if RSI < 30, consider oversold
        return 'BUY' if price_data.get('rsi', 50) < 30 else 'SELL'
