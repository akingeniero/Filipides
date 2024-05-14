
class TweetAnalyzer:
    def __init__(self, twitter_client, openai_client):
        self.twitter_client = twitter_client
        self.openai_client = openai_client

    async def fetch_and_analyze_tweets(self, user_id):
        tweets = await self.twitter_client.get_user_tweets(user_id)
        tweet_data_list = self.process_tweets(tweets)
        review = self.generate_review(tweet_data_list)
        analysis = self.openai_client.analyze_tweets(review)
        self.save_analysis(analysis, "analisis_sentimiento.txt")

    @staticmethod
    def process_tweets(tweets):
        tweet_data_list = []
        for tweet in tweets:
            tweet_data = {
                "id": tweet.id_str,
                "url": tweet.url,
                "date": tweet.date,
                "username": tweet.user.username,
                "displayname": tweet.user.displayname,
                "rawContent": tweet.rawContent,
                "engagement": {
                    "replyCount": tweet.replyCount,
                    "retweetCount": tweet.retweetCount,
                    "likeCount": tweet.likeCount,
                    "quoteCount": tweet.quoteCount
                },
                "lang": tweet.lang,
                "mentionedUsers": [user.username for user in tweet.mentionedUsers],
                "hashtags": tweet.hashtags
            }
            tweet_data_list.append(tweet_data)
        return tweet_data_list

    @staticmethod
    def generate_review(tweet_data_list):
        review = ""
        for tweet in tweet_data_list:
            review += (f'Tweet de {tweet["displayname"]} (@{tweet["username"]}) el '
                       f'{tweet["date"]}:\n{tweet["rawContent"]}\n')
        return review[:2000]

    @staticmethod
    def save_analysis(analysis, file_path):
        with open(file_path, "w") as file:
            file.write(analysis.strip())