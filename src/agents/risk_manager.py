# File: src/agents/risk_manager.py
import pandas as pd
from tools.api import get_market_data

class RiskManager:
    def __init__(self, max_drawdown_threshold=0.2, volatility_threshold=0.3):
        self.max_drawdown_threshold = max_drawdown_threshold
        self.volatility_threshold = volatility_threshold

    def calculate_max_drawdown(self, prices):
        rolling_max = prices.cummax()
        drawdown = (prices - rolling_max) / rolling_max
        return drawdown.min()

    def calculate_volatility(self, returns):
        return returns.std()

    def evaluate_risk(self, crypto_data):
        risk_assessment = {}
        for symbol, data in crypto_data.items():
            prices = data['close']
            returns = prices.pct_change().dropna()

            max_drawdown = self.calculate_max_drawdown(prices)
            volatility = self.calculate_volatility(returns)

            risk_level = "low"
            if max_drawdown < -self.max_drawdown_threshold or volatility > self.volatility_threshold:
                risk_level = "high"

            risk_assessment[symbol] = {
                "max_drawdown": max_drawdown,
                "volatility": volatility,
                "risk_level": risk_level,
            }

        return risk_assessment

    def analyze_risk(self, crypto_symbols):
        crypto_data = {symbol: get_market_data(symbol) for symbol in crypto_symbols}
        risk_assessment = self.evaluate_risk(crypto_data)
        return risk_assessment

if __name__ == "__main__":
    risk_manager = RiskManager()
    risks = risk_manager.analyze_risk(['BTCUSDT', 'ETHUSDT', 'BNBUSDT'])
    print("Risk Assessment:")
    print(risks)
