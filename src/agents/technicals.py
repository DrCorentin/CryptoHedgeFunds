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
        if prices.empty:
            raise ValueError("Price data is empty.")
        ma = {}
        for period in self.moving_average_periods:
            if len(prices) < period:
                raise ValueError(f"Not enough data points for moving average period: {period}")
            ma[f"ma_{period}"] = prices.rolling(window=period).mean()
        return pd.DataFrame(ma)

    def calculate_rsi(self, prices):
        if prices.empty:
            raise ValueError("Price data is empty.")
        if len(prices) < self.rsi_period:
            raise ValueError(f"Not enough data points for RSI period: {self.rsi_period}")
        delta = prices.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=self.rsi_period, min_periods=1).mean()
        avg_loss = loss.rolling(window=self.rsi_period, min_periods=1).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_macd(self, prices):
        if prices.empty:
            raise ValueError("Price data is empty.")
        if len(prices) < self.macd_slow:
            raise ValueError(f"Not enough data points for MACD slow period: {self.macd_slow}")
        ema_fast = prices.ewm(span=self.macd_fast, adjust=False).mean()
        ema_slow = prices.ewm(span=self.macd_slow, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=self.macd_signal, adjust=False).mean()
        macd_histogram = macd_line - signal_line
        return pd.DataFrame({
            'macd_line': macd_line,
            'signal_line': signal_line,
            'macd_histogram': macd_histogram
        })

    def fetch_and_calculate_technicals(self, symbol, start_date, end_date):
        prices = get_historical_data(symbol, start_date, end_date)
        if prices.empty:
            raise ValueError(f"No historical data fetched for symbol: {symbol}")
        moving_averages = self.calculate_moving_averages(prices['close'])
        rsi = self.calculate_rsi(prices['close'])
        macd = self.calculate_macd(prices['close'])
        technicals = pd.concat([moving_averages, rsi.rename('rsi'), macd], axis=1)
        return technicals
