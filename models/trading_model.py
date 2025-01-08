# File: src/models/trading_model.py

class TradingModel:
    def predict(self, data_point):
        """
        Predicts the trading signal for a given data point.

        :param data_point: A dictionary containing market data.
        :return: A trading signal ('buy', 'sell', or 'hold').
        """
        # Example logic: Buy if price_change is positive, sell if negative
        price_change = data_point.get("price_change", 0)
        if price_change > 0:
            return "buy"
        elif price_change < 0:
            return "sell"
        else:
            return "hold"
