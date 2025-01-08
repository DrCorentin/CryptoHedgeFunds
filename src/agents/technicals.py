# File: src/agents/technicals.py
import pandas as pd
import numpy as np
from tools.api import get_historical_data

class TechnicalsAgent:
    def __init__(self, moving_average_periods=(20, 50), rsi_period=14, macd_fast=12, macd_slow=26, macd_signal=9):
        self.moving_average_periods = moving_average_periods
        self.rsi_period = rsi_period
        self.macd_fast = macd_fast
        self.macd_slow = macd_slow
        self.macd_signal = macd_signal

    def calculate_moving_averages(self, prices):
        ma = {}
        for period in self.moving_average_periods:
            ma[f"ma_{period}"] = prices.rolling(window=period).mean()
        return pd.DataFrame(ma)

    def calculate_rsi(self, prices):
        delta = prices.diff()
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)
        avg_gain = pd.Series(gain).rolling(window=self.rsi_period).mean()
        avg_loss = pd.Series(loss).rolling(window=self.rsi_period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return pd.Series(rsi, name="rsi")

    def calculate_macd(self, prices):
        ema_fast = prices.ewm(span=self.macd_fast, adjust=False).mean()
        ema_slow = prices.ewm(span=self.macd_slow, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=self.macd_signal, adjust=False).mean()
        macd_histogram = macd_line - signal_line
        return pd.DataFrame({
            "macd_line": macd_line,
            "signal_line": signal_line,
            "macd_histogram": macd_histogram
        })

    def analyze_technical_indicators(self, historical_data):
        historical_data['moving_averages'] = self.calculate_moving_averages(historical_data['close'])
        historical_data['rsi'] = self.calculate_rsi(historical_data['close'])
        historical_data = pd.concat(
            [historical_data, self.calculate_macd(historical_data['close'])],
            axis=1
        )
        return historical_data

    def evaluate(self, crypto_symbols):
        signals = {}
        for symbol in crypto_symbols:
            # Fetch historical data
            historical_data = get_historical_data(symbol)

            # Calculate indicators
            analysis = self.analyze_technical_indicators(historical_data)

            # Generate signals (basic logic)
            latest = analysis.iloc[-1]
            signal = "neutral"
            if latest['rsi'] < 30:
                signal = "bullish"  # Oversold condition
            elif latest['rsi'] > 70:
                signal = "bearish"  # Overbought condition

            # Add MACD confirmation
            if latest['macd_line'] > latest['signal_line']:
                macd_signal = "bullish"
            else:
                macd_signal = "bearish"

            signals[symbol] = {
                "signal": signal,
                "rsi": latest['rsi'],
                "macd_signal": macd_signal,
                "macd_histogram": latest['macd_histogram']
            }

        return signals

if __name__ == "__main__":
    agent = TechnicalsAgent()
    technicals = agent.evaluate(['BTCUSDT', 'ETHUSDT', 'BNBUSDT'])
    print("Technical Analysis:")
    print(technicals)
