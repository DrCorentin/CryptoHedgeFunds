import pandas as pd
from tools.api import get_market_data

class ValuationAgent:
    def __init__(self, discount_rate=0.10, growth_rate=0.05, terminal_growth_rate=0.02, num_years=5):
        self.discount_rate = discount_rate
        self.growth_rate = growth_rate
        self.terminal_growth_rate = terminal_growth_rate
        self.num_years = num_years

    def calculate_intrinsic_value(self, crypto_data):
        """
        Calculates the intrinsic value of cryptocurrencies using DCF and network activity.
        
        Args:
            crypto_data: DataFrame containing cryptocurrency data with required columns:
                - 'symbol': Cryptocurrency symbol
                - 'volume': Recent trading volume
        
        Returns:
            DataFrame with 'symbol' and calculated 'intrinsic_value'.
        """
        # Placeholder for actual FCF calculation; use volume as a proxy
        crypto_data['free_cash_flow'] = crypto_data['volume'] * 0.5  # Mock logic

        # Calculate DCF for each crypto
        crypto_data['dcf_value'] = crypto_data.apply(
            lambda row: self._calculate_dcf(row['free_cash_flow']),
            axis=1
        )

        # Network activity score as a secondary valuation metric
        crypto_data['network_activity_value'] = crypto_data['volume'] * 0.3  # Placeholder logic

        # Combine DCF and network activity for intrinsic value
        crypto_data['intrinsic_value'] = (
            0.7 * crypto_data['dcf_value'] +
            0.3 * crypto_data['network_activity_value']
        )

        return crypto_data[['symbol', 'intrinsic_value']]

    def _calculate_dcf(self, free_cash_flow):
        """Helper to calculate DCF value."""
        # Project future cash flows
        cash_flows = [free_cash_flow * (1 + self.growth_rate) ** i for i in range(self.num_years)]

        # Calculate present values of cash flows
        present_values = [
            cf / (1 + self.discount_rate) ** (i + 1)
            for i, cf in enumerate(cash_flows)
        ]

        # Terminal value
        terminal_value = (
            cash_flows[-1] * (1 + self.terminal_growth_rate) /
            (self.discount_rate - self.terminal_growth_rate)
        )
        terminal_value_discounted = terminal_value / (1 + self.discount_rate) ** self.num_years

        # Total intrinsic value
        return sum(present_values) + terminal_value_discounted

    def evaluate(self):
        """
        Fetch market data from Binance API and perform valuation.
        
        Returns:
            DataFrame with 'symbol' and 'intrinsic_value'.
        """
        market_data = get_market_data()
        valuation = self.calculate_intrinsic_value(market_data)
        return valuation

if __name__ == "__main__":
    agent = ValuationAgent()
    valuations = agent.evaluate()
    print("Valuation Results:")
    print(valuations)