from agents.identifier import IdentifierAgent
from agents.valuation import ValuationAgent
from agents.sentiment import SentimentAgent
from agents.fundamentals import FundamentalsAgent
from agents.technicals import TechnicalsAgent
from agents.risk_manager import RiskManager
from agents.portfolio_manager import PortfolioManager
from tools.api import get_market_data
from backtester import Backtester


def main():
    print("Starting AI Crypto Hedge Fund...")

    # Phase 1: Training the model
    print("Phase 1: Training models...")
    market_data = get_market_data()
    print("Market Data Sample:", list(market_data.items())[:5])  # Debugging output

    identifier = IdentifierAgent()
    high_potential_cryptos = identifier.identify(market_data)

    if not high_potential_cryptos:
        print("No high-potential cryptocurrencies identified. Exiting...")
        return

    print("High-Potential Cryptos Identified:", high_potential_cryptos)

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

    # Simulate trades
    trades = portfolio_manager.generate_orders(portfolio)
    backtester = Backtester()
    backtester.simulate(trades)

    # Phase 3: Production Mode
    print("Phase 3: Running in production...")
    # Add live trading logic here using APIs (Binance or PancakeSwap)


if __name__ == "__main__":
    main()
