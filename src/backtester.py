# File: src/backtester.py

class Backtester:
    def __init__(self, model, historical_data):
        """
        Initialize the Backtester.

        :param model: The trained model to evaluate.
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
            actual_signal = data_point["actual_signal"]  # Replace with your actual signal field
            predicted_signal = self.model.predict(data_point)

            # Compare predictions with actual signals
            self.total_predictions += 1
            if predicted_signal == actual_signal:
                self.correct_predictions += 1

            # Calculate and display accuracy
            accuracy = (self.correct_predictions / self.total_predictions) * 100
            print(f"\raccuracy... {accuracy:.2f}%", end="", flush=True)

        print()  # Add a newline after the loop for clean output

    def report(self):
        """
        Generate a report of the backtest results.
        """
        cumulative_return = sum(
            self.simulate_trade(data_point, self.model.predict(data_point))
            for data_point in self.historical_data
        )
        accuracy = (self.correct_predictions / self.total_predictions) * 100

        print("\nBacktesting Report:")
        print(f"Total Trades: {self.total_predictions}")
        print(f"Correct Predictions: {self.correct_predictions}")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Cumulative Return: {cumulative_return:.2f}")

    def simulate_trade(self, data_point, predicted_signal):
        """
        Simulate a trade based on the predicted signal.

        :param data_point: A single data point from historical data.
        :param predicted_signal: The model's predicted trading signal.
        :return: Simulated profit/loss for the trade.
        """
        if predicted_signal == "buy":
            return data_point["price_change"]  # Example profit metric
        elif predicted_signal == "sell":
            return -data_point["price_change"]
        else:  # Hold
            return 0
