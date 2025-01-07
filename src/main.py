from agents.identifier import IdentifierAgent
from agents.valuation import ValuationAgent
from agents.sentiment import SentimentAgent
from agents.fundamentals import FundamentalsAgent
from agents.technicals import TechnicalsAgent
from agents.risk_manager import RiskManager
from agents.portfolio_manager import PortfolioManager
from tools.api import APIClient
from tools.utils import ensure_directories
from backtester import Backtester

def main():
    print("Starting AI Crypto Hedge Fund...")
    ensure_directories()

    # Phase 1: Training
    print("Phase 1: Training models...")
    api_client = APIClient()  # Initialize the API client to fetch market data
    market_data = api_client.fetch_market_data()  # Fetch real-time market data

    # Initialize all agents
    identifier = IdentifierAgent()
    valuation = ValuationAgent()
    sentiment = SentimentAgent()
    fundamentals = FundamentalsAgent()
    technicals = TechnicalsAgent()
    risk_manager = RiskManager()
    portfolio_manager = PortfolioManager()

    # AI identifies and evaluates cryptos
    identified_cryptos = identifier.identify_cryptos(market_data)  # Identify cryptos based on market data
    evaluated_cryptos = []  # This will store the evaluated cryptocurrencies with all calculated metrics

    # Evaluate each identified crypto
    for crypto in identified_cryptos:
        # For each identified crypto, calculate metrics based on your agents
        intrinsic_value = valuation.calculate_intrinsic_value(crypto)  # Intrinsic value calculation
        sentiment_score = sentiment.analyze_sentiment(crypto)  # Sentiment analysis
        fundamentals_score = fundamentals.analyze_fundamentals(crypto)  # Fundamentals analysis
        technical_signal = technicals.analyze_technical_indicators(crypto)  # Technical analysis
        
        # Construct the evaluated crypto data
        evaluated_cryptos.append({
            'symbol': crypto['symbol'],
            'intrinsic_value': intrinsic_value,
            'sentiment': sentiment_score,
            'fundamentals': fundamentals_score,
            'technical_signal': technical_signal,
            'price': float(crypto['lastPrice']) if crypto['lastPrice'] != '0.00' else 0,  # Check if the price is non-zero
        })

    # Portfolio allocation based on fund size
    portfolio_manager.evaluate_fund_size(5000)  # Example starting balance in EUR

    # Modify: Loop through evaluated cryptos and update the portfolio with each crypto's trade price
    selected_cryptos = []
    for crypto in evaluated_cryptos:
        trade_price = crypto['price']  # Get the real-time price for the crypto

        if trade_price == 0:
            print(f"Skipping {crypto['symbol']} due to zero price.")
            continue  # Skip cryptos with a price of 0 to avoid division by zero

        # Create the trade details with 'from' and 'to' keys
        trade_details = {
            'from': 'EUR',  # Assuming the trade is being made from EUR
            'to': crypto['symbol'],  # The crypto being bought/sold
            'amount': 50 / trade_price,  # Amount to trade based on available balance (example)
        }

        # Update the portfolio with the trade details
        updated_portfolio = portfolio_manager.update_portfolio(trade_details, trade_price)  # Pass both the trade details and trade price

        if updated_portfolio is None:
            print(f"Skipping {crypto['symbol']} due to None returned from update_portfolio.")
            continue  # Skip this iteration if update_portfolio returns None

        selected_cryptos.append(updated_portfolio)

    # Phase 2: Simulating trades
    print("Phase 2: Simulating trades...")
    backtester = Backtester(starting_balance=50)  # Start with 50 EUR for backtesting
    for crypto in selected_cryptos:
        if crypto is not None:
            trade_amount = backtester.calculate_trade_amount(crypto)  # Calculate trade amount for the selected crypto
            trade_price = crypto['price']  # Use the current price for the trade
            backtester.simulate_trade('EUR', crypto['symbol'], trade_amount, trade_price)  # Simulate the trade

    backtester.save_results()  # Save backtest results
    print("Simulation complete. Results saved.")

if __name__ == "__main__":
    main()
