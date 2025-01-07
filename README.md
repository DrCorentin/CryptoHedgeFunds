# Prompt Instructions

I want to develop an AI crypto hedge fund with trading. 
The development will be phased to allow proper deployment and testing. 

1. Set-up the learning model (ultimatelly used to make trading decisions)
2. In a test mode, simulate the trading (assumed the order will be executed). this is NOT done in production. Just get them on excel CSV (timestamp, devise from / to : fiat/crypto, price, cumulative return in euro, in btc and in percentage since fund start date)
3. in production mode. 

I want this AI-powered hedge fund to be train and runing. How can I ensure this run properly and keep past learning? 
I want you to write the code for each component, fully functionable. The data will be sourced from Binance and pancakeswap. 
You can look at the following link "https://github.com/virattt/ai-hedge-fund" to see the each component code. 


# CryptoHedgeFunds

This is a proof concept for an AI-powered crypto hedge fund.  The goal of this project is to explore the use of AI to make trading decisions and to execute them.  This project is for **educational** purposes only and is not intended for real profit.


## BTC Strategy in function of Asset size

I want the fund to be split as follow:  (minimum percentage to hold in BTC)
1. asset under 5k: no minimum in BTC
2. asset from 5k to 10k: 20% in BTC
3. asset from 10k to 50k: 30% in BTC
4. asset from 50k to 150k: 40% in BTC
5. asset above 150k: 50% in BTC

The remaining should be invested in maximum 5 cryptos, identified by the AI as having the highest return potential. 


## List of Agents 

This system employs several agents working together:

1. Identifier Agent - Identified high gain potential crypto (identified 10 high return potential cryptos and 5 will be selected by the portofolio manager based on outcomme from the remaining agents)
2. Valuation Agent - Calculates the intrinsic value of a crypto and generates trading signals
3. Sentiment Agent - Analyzes market sentiment and generates trading signals
4. Fundamentals Agent - Analyzes fundamental data and generates trading signals
5. Technical Analyst - Analyzes technical indicators and generates trading signals
6. Risk Manager - Calculates risk metrics and sets position limits
7. Portfolio Manager - Makes final trading decisions and generates orders
   

## Project Structure

```
ai-crypto-hedge-fund/
├── src/
│   ├── agents/                   # Agent definitions and workflows
│   │   ├── identifier.py         # Crypto Identifier agent
│   │   ├── valuation.py          # Valuation analysis agent
│   │   ├── sentiment.py          # Sentiment analysis agent
│   │   ├── fundamentals.py       # Fundamental analysis agent
│   │   ├── technicals.py         # Technical analysis agent
│   │   ├── risk_manager.py       # Risk management agent
│   │   ├── portfolio_manager.py  # Portfolio management agent
│   ├── tools/                    # Supporting tools
│   │   ├── api.py                # API connection tools
│   │   ├── utils.py              # Utility functions
│   ├── backtester.py             # Backtesting functionality
│   ├── main.py                   # Main entry point
├── data/                         # Dataset and logs storage
│   ├── historical/               # Historical market data
│   ├── logs/                     # Logs of the execution
├── models/                       # Model storage
│   ├── trained_model.pkl         # Saved ML model
├── pyproject.toml                # Python project dependencies
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies

```





