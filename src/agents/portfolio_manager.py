# File: src/agents/portfolio_manager.py

import pandas as pd

class PortfolioManager:
    def __init__(self, api_client):
        """
        Initializes the Portfolio Manager with a given API client.

        :param api_client: An object to interact with the Binance API.
        """
        self.api_client = api_client

    def generate_recommendations(self, high_potential_cryptos, total_assets=10_000):
        """
        Generates trading recommendations based on asset size and high-potential cryptos.

        :param high_potential_cryptos: DataFrame of high-potential cryptos identified by the identifier agent.
        :param total_assets: The total value of the portfolio in EUR.
        :return: A DataFrame containing trading recommendations.
        """
        # Validate symbols before generating recommendations
        available_symbols = self.get_available_symbols()

        btc_allocation = self.calculate_btc_allocation(total_assets)
        btc_prices = self.fetch_price_info("BTCUSDT")
        btc_volume = btc_allocation / btc_prices['last_price']

        remaining_allocation = total_assets - btc_allocation
        allocation_per_crypto = remaining_allocation / 5

        recommendations = [{"pair": "BTC/EUR", "strategy": "buy", "volume": btc_volume, "allocation": btc_allocation}]

        for _, crypto in high_potential_cryptos.head(5).iterrows():
            symbol = crypto['symbol']
            if symbol not in available_symbols:
                print(f"Skipping unavailable symbol: {symbol}")
                continue

            crypto_prices = self.fetch_price_info(symbol)
            crypto_volume = allocation_per_crypto / crypto_prices['last_price']
            recommendations.append({
                "pair": f"{symbol}/EUR",
                "strategy": "buy",
                "volume": crypto_volume,
                "allocation": allocation_per_crypto
            })

        return pd.DataFrame(recommendations)

    def get_available_symbols(self):
        """
        Fetches a list of all available symbols on Binance.

        :return: A set of available trading symbols.
        """
        exchange_info = self.api_client.client.get_exchange_info()
        return {symbol['symbol'] for symbol in exchange_info['symbols']}

    def calculate_btc_allocation(self, total_assets):
        """
        Calculates the BTC allocation based on the total asset size.

        :param total_assets: The total value of the portfolio in EUR.
        :return: The BTC allocation in EUR.
        """
        if total_assets < 5_000:
            return 0
        elif total_assets < 10_000:
            return total_assets * 0.2
        elif total_assets < 50_000:
            return total_assets * 0.3
        elif total_assets < 150_000:
            return total_assets * 0.4
        else:
            return total_assets * 0.5

    def fetch_price_info(self, symbol):
        """
        Fetches price information (last price, bid price, ask price) of a given trading pair.

        :param symbol: The trading pair (e.g., "BTCUSDT").
        :return: A dictionary containing 'last_price', 'bid_price', and 'ask_price'.
        """
        price_info = self.api_client.get_ticker_info(symbol)
        if not price_info:
            raise ValueError(f"Unable to fetch price data for {symbol}")
        return price_info
