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


## Presicion for avoidance of doubt

2 models will be connected. Small precision, one model will solely be a learning model to identified trading patern and make recommendation (as buy, hold, sell), but will not make the trading itself. 

one will be learning and making trading recommendation - use public API
one will be executing the trade - use private API (to perform the trade)

** all connection with the model 2 will be placeholder at the moment **

1. the learning model should have the most important place and be continuous (required to identified tradinc decision: buy / hold / sell). 
2. I want to use public API for the learning model. The trading would be call through a different python model. 
3. each trading recommendation will be saved in a specific csv folder. 

the model will be split as follow: 
identified crypto with higher possible return, based on the following criteria: trading volume in the last 24h, bid volume, ask volume, bid price and ask price (to identify if it is mostly buy or sell signal). Can the crypto ticket (name of the crypto as BTC) and community engagement of official channels (X - formerly twitter, facebook, telegram...) an active community might present better return. Most important, it should be a liquid crypto pair. 
When the model is doing a recommendation (the learning never stop), it should provide the following information: strategy (buy, hold, sell), the pair (crypto / fiat, crypto / crypto) and also provide volume (in percentage) to be bought. When it is crypto to crypto (example BTC / ETH), the model should estimate what would be the highest return between doing nothing or selling ETH to buy BTC if there was not ETH sell recommendation. (what is stronger, ETH hold or BTC buy). 

BTC can be sold, but we try to keep a BTC base. 

### ideas for the model features and structure
learning (this is the learning to identify how the market works, what is triggering price movement and is potentially source of profit). This is a learning model (and should be regularly. 
Binance API docs can be founds there: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
This is to ensure no error arise due to incorrect argument call in the API. 


current source code: https://github.com/DrCorentin/CryptoHedgeFunds/
Maybe, there should be 3 distincts modules/models (learning pattern, trading recommendation and trading execution). 

#### Code to be updated should ALWAYS be displayed in full (not just the adjustment) and should include file name. 
















