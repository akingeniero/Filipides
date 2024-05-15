import os

import aiofiles


class TweetAnalyzer:
    """
    TweetAnalyzer is responsible for fetching, processing, and analyzing tweets.

    Attributes:
        twitter_client (TwitterClient): An instance of a Twitter client for fetching tweets.
        openai_client (OpenAIClient): An instance of an OpenAI client for analyzing tweets.
    """

    def __init__(self, twitter_client, openai_client):
        """
        Initializes the TweetAnalyzer with the given Twitter and OpenAI clients.

        Args:
            twitter_client (TwitterClient): An instance of a Twitter client for fetching tweets.
            openai_client (OpenAIClient): An instance of an OpenAI client for analyzing tweets.
        """
        self.twitter_client = twitter_client
        self.openai_client = openai_client

    async def fetch_and_analyze_tweets(self, user_id):
        """
        Fetches tweets for a given user and performs sentiment analysis on them.

        Args:
            user_id (int): The ID of the user whose tweets are to be fetched and analyzed.

        Returns:
            None
        """
        tweets = await self.twitter_client.get_user_tweets(user_id)
        tweet_data_list = await self.process_tweets(tweets)
        review = self.generate_review(tweet_data_list)
        analysis = self.openai_client.analyze_tweets(review)
        self.save_analysis(analysis, f"{user_id}.txt")

    @staticmethod
    async def process_tweets(tweets_coroutine):
        """
        Processes a list of tweets and extracts relevant data.

        Args:
            tweets_coroutine (list): A list of tweet objects.

        Returns:
            list: A list of dictionaries containing processed tweet data.
        """
        tweet_data_list = []
        tweets = await tweets_coroutine
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
        """
        Generates a review text from a list of processed tweet data.

        Args:
            tweet_data_list (list): A list of dictionaries containing processed tweet data.

        Returns:
            str: A review text based on the tweet data.
        """
        review = ""
        for tweet in tweet_data_list:
            review += (f'Tweet by {tweet["displayname"]} (@{tweet["username"]}) on '
                       f'{tweet["date"]}:\n{tweet["rawContent"]}\n')
        return review[:2000]

    @staticmethod
    def save_analysis(analysis, filename):
        """
        Saves the analysis result to a file.

        Args:
            analysis (str): The analysis result to be saved.
            filename (str): The path of the file where the analysis will be saved.

        Returns:
            None
        """
        file_path = filename
        if os.path.exists(file_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(file_path):
                file_path = f"{base}_{counter}{ext}"
                counter += 1

        with open(file_path, 'w') as file:
            file.write(analysis.strip())
