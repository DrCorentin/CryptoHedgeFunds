class PortfolioManager:
    def __init__(self):
        self.starting_balance_eur = 0
        self.crypto_holdings = {}  # Example: {'BTC': 0.1, 'ETH': 2.0}
        self.fiat_balance_eur = 0

    def initialize_portfolio(self, starting_balance):
        """Initialize the portfolio with a starting balance."""
        self.starting_balance_eur = starting_balance
        self.fiat_balance_eur = starting_balance
        print(f"Portfolio initialized with EUR balance: {self.fiat_balance_eur}")

    def evaluate_fund_size(self, current_prices):
        """
        Calculate the total fund value in EUR.
        :param current_prices: Dictionary of crypto prices in EUR.
                               Example: {'BTC': 25000, 'ETH': 1500}
        """
        total_crypto_value_eur = sum(
            self.crypto_holdings[crypto] * current_prices.get(crypto, 0)
            for crypto in self.crypto_holdings
        )
        total_fund_size_eur = self.fiat_balance_eur + total_crypto_value_eur
        print(f"Current fiat balance: {self.fiat_balance_eur} EUR")
        print(f"Current crypto holdings value: {total_crypto_value_eur} EUR")
        print(f"Total fund size: {total_fund_size_eur} EUR")
        return total_fund_size_eur

    def update_portfolio(self, trade_details, trade_price):
        """
        Update the portfolio after a trade.
        :param trade_details: Dictionary with trade info.
                              Example: {'from': 'EUR', 'to': 'BTC', 'amount': 500}
        :param trade_price: The price of the traded asset in EUR.
        """
        from_asset = trade_details['from']
        to_asset = trade_details['to']
        amount = trade_details['amount']

        if from_asset == 'EUR':
            self.fiat_balance_eur -= amount
            self.crypto_holdings[to_asset] = self.crypto_holdings.get(to_asset, 0) + (amount / trade_price)
        elif to_asset == 'EUR':
            self.fiat_balance_eur += amount * trade_price
            self.crypto_holdings[from_asset] -= amount
        else:
            self.crypto_holdings[from_asset] -= amount
            self.crypto_holdings[to_asset] = self.crypto_holdings.get(to_asset, 0) + (amount * trade_price)

        print(f"Updated portfolio: Fiat - {self.fiat_balance_eur} EUR, Crypto - {self.crypto_holdings}")
