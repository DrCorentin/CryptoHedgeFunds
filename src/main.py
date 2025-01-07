from src.agents.identifier import IdentifierAgent
from src.agents.valuation import ValuationAgent
from src.agents.sentiment import SentimentAgent
from src.agents.fundamentals import FundamentalsAgent
from src.agents.technicals import TechnicalsAgent
from src.agents.risk_manager import RiskManager
from src.agents.portfolio_manager import PortfolioManager
from src.tools.api import get_market_data
from src.backtester import Backtester

def main():
    print("Starting AI Crypto Hedge Fund...")

    # Phase 1: Training the model
    print("Phase 1: Training models...")
    market_data = get_market_data()
    identifier = IdentifierAgent()
    high_potential_cryptos = identifier.identify(market_data)

    # Phase 2: Test Mode (Simulated Trading)
    print("Phase 2: Simulating trades...")
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
    print("Portfolio allocation:")
    print(portfolio)

    # Phase 3: Production Mode
    print("Phase 3: Running in production...")
    # Implement live trading logic here using Binance API

if __name__ == "__main__":
    main()
