class ValuationAgent:
    def analyze(self, crypto):
        # Perform valuation analysis using intrinsic value methods
        intrinsic_value = crypto['price'] * (1 + crypto['growth_rate'])
        market_value = crypto['market_cap']
        valuation_gap = (intrinsic_value - market_value) / market_value

        signal = "bullish" if valuation_gap > 0.15 else "bearish" if valuation_gap < -0.15 else "neutral"
        return {"crypto": crypto['symbol'], "signal": signal, "gap": valuation_gap}
