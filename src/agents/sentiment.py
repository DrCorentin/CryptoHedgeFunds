class SentimentAgent:
    def analyze_sentiment(self, social_data):
        # Dummy logic: Positive sentiment if keyword count > threshold
        positive_score = social_data.get('positive_mentions', 0)
        negative_score = social_data.get('negative_mentions', 0)
        return positive_score - negative_score
