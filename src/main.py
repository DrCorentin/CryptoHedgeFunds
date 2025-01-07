from src.agents.identifier import IdentifierAgent
from src.agents.valuation import ValuationAgent
from src.agents.sentiment import SentimentAgent
from src.agents.fundamentals import FundamentalsAgent
from src.agents.technicals import TechnicalsAgent
from src.agents.risk_manager import RiskManager
from src.agents.portfolio_manager import PortfolioManager
from src.tools.api import get_binance_ticker, get_pancakeswap_prices
from src.backtester import Backtester

def main():
    print("Starting AI Crypto Hedge Fund...")

    # Phase 1: Training the model
    print("\nPhase 1: Training models...")
    # Simulate fetching market data
    market_data = {
        "BTC": get_binance_ticker("BTCUSDT"),
        "ETH": get_binance_ticker("ETHUSDT"),
        "PancakeSwap": get_pancakeswap_prices()
    }

    identifier = IdentifierAgent()
    high_potential_cryptos = identifier.identify(market_data)
    print(f"High potential cryptos identified: {high_potential_cryptos}")

    # Phase 2: Test Mode (Simulated Trading)
    print("\nPhase 2: Simulating trades...")
    valuation = ValuationAgent()
    sentiment = SentimentAgent()
    fundamentals = FundamentalsAgent()
    technicals = TechnicalsAgent()
    risk_manager = RiskManager()
    portfolio_manager = PortfolioManager()

    signals = []
    for crypto in high_potential_cryptos:
        valuation_signal = valuation.analyze(crypto)
        sentiment_signal = sentiment.analyze(crypto)
        fundamentals_signal = fundamentals.analyze(crypto)
        technicals_signal = technicals.analyze(crypto)
        
        combined_signal = portfolio_manager.combine_signals(
            valuation_signal,
            sentiment_signal,
            fundamentals_signal,
            technicals_signal
        )
        signals.append(combined_signal)

    portfolio = portfolio_manager.allocate(signals)
    print("\nPortfolio allocation:")
    print(portfolio)

    # Backtesting
    backtester = Backtester()
    for asset, allocation in portfolio.items():
        backtester.simulate_trade("EUR", asset, allocation)

    backtester.save_results()

    # Phase 3: Production Mode (Placeholder)
    print("\nPhase 3: Running in production...")
    print("This phase is not yet implemented. Use APIs for live trading logic.")

if __name__ == "__main__":
    main()
