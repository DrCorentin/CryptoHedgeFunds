# File: src/agents/portfolio_manager.py
import pandas as pd

class PortfolioManager:
    def __init__(self, allocation_strategy="risk_adjusted", max_allocation=0.4):
        self.allocation_strategy = allocation_strategy
        self.max_allocation = max_allocation

    def calculate_allocations(self, crypto_data, risk_assessment):
        """
        Calculate portfolio allocations based on risk-adjusted returns or other strategies.
        """
        allocations = {}
        total_score = 0

        for symbol in crypto_data.keys():
            risk_level = risk_assessment[symbol]['risk_level']
            intrinsic_value = crypto_data[symbol]['intrinsic_value']

            # Risk-adjusted scoring
            if risk_level == "low":
                score = intrinsic_value * 1.5
            else:
                score = intrinsic_value * 0.5

            allocations[symbol] = score
            total_score += score

        # Normalize allocations
        for symbol in allocations:
            allocations[symbol] = min(self.max_allocation, allocations[symbol] / total_score)

        return allocations

    def manage_portfolio(self, crypto_data, risk_assessment):
        allocations = self.calculate_allocations(crypto_data, risk_assessment)
        return allocations

if __name__ == "__main__":
    # Mock data
    crypto_data = {
        "BTCUSDT": {"intrinsic_value": 80000},
        "ETHUSDT": {"intrinsic_value": 4000},
        "BNBUSDT": {"intrinsic_value": 400},
    }
    risk_assessment = {
        "BTCUSDT": {"risk_level": "low"},
        "ETHUSDT": {"risk_level": "medium"},
        "BNBUSDT": {"risk_level": "high"},
    }

    portfolio_manager = PortfolioManager()
    allocations = portfolio_manager.manage_portfolio(crypto_data, risk_assessment)
    print("Portfolio Allocations:")
    print(allocations)
