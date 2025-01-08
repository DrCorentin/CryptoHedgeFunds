import requests
from tools.api import get_social_sentiment, get_news_sentiment

class SentimentAgent:
    def __init__(self):
        pass

    def analyze_sentiment(self, crypto_symbols):
        sentiment_scores = {}
        for symbol in crypto_symbols:
            # Fetch sentiment scores from multiple sources
            social_sentiment = get_social_sentiment(symbol)
            news_sentiment = get_news_sentiment(symbol)

            # Weighted average of sentiment sources
            sentiment_scores[symbol] = (
                social_sentiment * 0.6 + news_sentiment * 0.4
            )
        return sentiment_scores

if __name__ == "__main__":
    agent = SentimentAgent()
    sentiment = agent.analyze_sentiment(['BTC', 'ETH', 'BNB'])
    print("Sentiment Analysis:")
    print(sentiment)