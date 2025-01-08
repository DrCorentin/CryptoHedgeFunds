# File: src/tools/api.py

from binance.client import Client

class BinanceAPI:
    def __init__(self, api_key=None, api_secret=None):
        """
        Initializes the Binance API client.

        :param api_key: Binance API key (optional for public data).
        :param api_secret: Binance API secret (optional for public data).
        """
        self.client = Client(api_key, api_secret)


    def get_ticker_info(self, symbol):
        """
        Fetches the last price, bid price, and ask price for a specific trading pair.

        :param symbol: The trading pair symbol, e.g., "BTCUSDT".
        :return: A dictionary containing 'last_price', 'bid_price', and 'ask_price' as floats.
        """
        ticker = self.client.get_ticker(symbol=symbol)
        return {
            'last_price': float(ticker['lastPrice']),
            'bid_price': float(ticker['bidPrice']),
            'ask_price': float(ticker['askPrice'])
        }


    def get_ticker(self, symbol=None):
        """
        Fetches the 24-hour ticker price change statistics.

        :param symbol: (Optional) The trading pair symbol, e.g., "BTCUSDT". If None, fetches all tickers.
        :return: The ticker data as a dictionary or a list of dictionaries.
        """
        if symbol:
            return self.client.get_ticker(symbol=symbol)
        return self.client.get_ticker()

    def get_historical_klines(self, symbol, interval, start_str, end_str=None):
        """
        Fetches historical candlestick data (OHLCV) for a trading pair.

        :param symbol: The trading pair symbol, e.g., "BTCUSDT".
        :param interval: Kline interval, e.g., "1h", "1d".
        :param start_str: Start time in string format, e.g., "1 Jan, 2020".
        :param end_str: (Optional) End time in string format.
        :return: A list of OHLCV data.
        """
        return self.client.get_historical_klines(symbol, interval, start_str, end_str)

    def get_current_price(self, symbol):
        """
        Fetches the current price for a specific trading pair.

        :param symbol: The trading pair symbol, e.g., "BTCUSDT".
        :return: The current price as a float.
        """
        ticker = self.client.get_symbol_ticker(symbol=symbol)
        return float(ticker["price"])
