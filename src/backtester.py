# File: src/backtester.py

class Backtester:
    def __init__(self, model, historical_data):
        """
        Initialize the Backtester.

        :param model: The model to evaluate (must have a predict method).
        :param historical_data: Historical data for backtesting.
        """
        self.model = model
        self.historical_data = historical_data
        self.correct_predictions = 0
        self.total_predictions = 0

    def run_backtest(self):
        """
        Run the backtest and calculate performance metrics.
        """
        for i, data_point in enumerate(self.historical_data, start=1):
            actual_signal = data_point["actual_signal"]
            predicted_signal = self.model.predict(data_point)

            # Track predictions for accuracy calculation
            self.total_predictions += 1
            if predicted_signal == actual_signal:
                self.correct_predictions += 1

            # Simulate the trade
            self.simulate_trade(data_point, predicted_signal)

            # Display continuous accuracy
            accuracy = (self.correct_predictions / self.total_predictions) * 100
            print(f"\raccuracy... {accuracy:.2f}%", end="", flush=True)
        print()

    def simulate_trade(self, data_point, predicted_signal):
        """
        Simulates a trade based on the predicted signal.

        :param data_point: A single data point from historical data.
        :param predicted_signal: The model's predicted trading signal.
        """
        # Simulate profit or loss based on signal
        price_change = data_point["price_change"]
        if predicted_signal == "buy":
            return price_change
        elif predicted_signal == "sell":
            return -price_change
        else:  # Hold
            return 0

    def report(self):
        """
        Generate a backtesting report.
        """
        accuracy = (self.correct_predictions / self.total_predictions) * 100
        print("\nBacktesting Report:")
        print(f"Total Predictions: {self.total_predictions}")
        print(f"Correct Predictions: {self.correct_predictions}")
        print(f"Accuracy: {accuracy:.2f}%")
