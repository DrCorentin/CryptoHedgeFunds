from src.tools.api import get_market_data

def main():
    print("Starting AI Crypto Hedge Fund...")

    # Phase 1: Training the model
    print("Phase 1: Training models...")
    market_data = get_market_data()
    if not market_data:
        print("Error: No market data available.")
        return
    identifier = IdentifierAgent()
    high_potential_cryptos = identifier.identify(market_data)

    # Phase 2: Test Mode (Simulated Trading)
    print("Phase 2: Simulating trades...")
    valuation = ValuationAgent()
    sentiment = SentimentAgent()
    fundamentals = FundamentalsAgent()
    technicals = TechnicalsAgent()
    portfolio_manager = PortfolioManager()
    backtester = Backtester()

    signals = []
    for crypto in high_potential_cryptos:
        valuation_signal = valuation.analyze(crypto)
        sentiment_signal = sentiment.analyze(crypto)
        fundamentals_signal = fundamentals.analyze(crypto)
        technicals_signal = technicals.analyze(crypto)
        combined_signal = portfolio_manager.combine_signals(
            valuation_signal, sentiment_signal, fundamentals_signal, technicals_signal
        )
        signals.append(combined_signal)

    portfolio = portfolio_manager.allocate(signals)
    print("Portfolio allocation:")
    print(portfolio)

    # Generate and simulate trades
    trades = portfolio_manager.generate_trades(portfolio)
    for trade in trades:
        backtester.simulate_trade(trade['from'], trade['to'], trade['amount'])

    backtester.save_results()

    # Output final balances
    print(f"Final Portfolio Value: {backtester.total_performance['EUR']} EUR")
    print(f"BTC Equivalent: {backtester.total_performance['BTC']} BTC")


if __name__ == "__main__":
    main()
