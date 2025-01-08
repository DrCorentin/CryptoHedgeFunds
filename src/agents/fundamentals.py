from tools.api import get_onchain_data

class FundamentalsAgent:
    def __init__(self):
        pass

    def analyze_fundamentals(self, crypto_data):
        # Fetch on-chain metrics
        onchain_data = get_onchain_data(crypto_data['symbol'].tolist())

        # Merge with provided data
        crypto_data = crypto_data.merge(onchain_data, on='symbol')

        # Scoring based on fundamental metrics
        crypto_data['fundamental_score'] = (
            crypto_data['transaction_volume'] * 0.4 +
            crypto_data['active_addresses'] * 0.3 +
            crypto_data['developer_activity'] * 0.3
        )

        return crypto_data[['symbol', 'fundamental_score']]

if __name__ == "__main__":
    agent = FundamentalsAgent()
    sample_data = pd.DataFrame({'symbol': ['BTC', 'ETH', 'BNB']})
    fundamentals = agent.analyze_fundamentals(sample_data)
    print("Fundamental Analysis:")
    print(fundamentals)