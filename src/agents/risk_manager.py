class RiskManager:
    def calculate_risk(self, portfolio):
        risk = sum([item['value'] for item in portfolio]) * 0.2
        return risk  # Example: 20% risk threshold
