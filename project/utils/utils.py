import json
import os
from datetime import datetime

from project.client.llm_client.llm_manager import LlmManager
from project.client.news_client import NewsClient
from project.client.twitter_client import TwitterClient


async def fetch_and_analyze_tweets(user_id: int) -> None:
    """
    Fetches tweets for a given user ID, processes the tweets, generates a review, and analyzes it using OpenAI.

    Args:
        user_id (int): The user ID to fetch tweets for.

    Returns:
        None
    """
    twitter_client = TwitterClient()
    llm_manager = LlmManager()
    tweets = await twitter_client.get_user_tweets(user_id)
    tweet_data_list = await process_tweets(tweets)
    review = generate_review(tweet_data_list)
    analysis, elapsed_time = llm_manager.analyze_tweets(review)
    inform = {
        "user_id": user_id,
        "review": review,
        "analysis": analysis,
        "elapsed_time": elapsed_time,
        "timestamp": datetime.now().isoformat()
    }
    inform_str = json.dumps(inform, indent=4, ensure_ascii=False)
    save_analysis(inform_str, f"{user_id}.json")


async def fetch_and_analyze_news(url_news: str) -> None:
    """
    Fetches the main news content from a given URL, generates a review, and analyzes it using OpenAI.

    Args:
        url_news (str): The URL of the news article to analyze.

    Returns:
        None
    """
    news_client = NewsClient()
    llm_manager = LlmManager()
    review = await news_client.extract_main_news(url_news)
    analysis, elapsed_time = llm_manager.analyze_news(review[:2000])
    inform = {
        "url": url_news,
        "review": review,
        "analysis": analysis,
        "elapsed_time": elapsed_time,
        "timestamp": datetime.now().isoformat()
    }
    inform_str = json.dumps(inform, indent=4, ensure_ascii=False)
    save_analysis(inform_str, f'{review[8:28]}.json')


async def process_tweets(tweets_coroutine) -> list:
    """
    Processes tweets by extracting relevant information into a structured format.

    Args:
        tweets_coroutine: Coroutine that fetches tweets.

    Returns:
        list: A list of dictionaries containing tweet data.
    """
    tweet_data_list = []
    tweets = await tweets_coroutine
    for tweet in tweets:
        tweet_data = {
            "id": tweet.id_str,
            "url": tweet.url,
            "date": tweet.date,
            "username": tweet.user.username,
            "displayName": tweet.user.displayname,
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


def generate_review(tweet_data_list: list) -> str:
    """
    Generates a review string from a list of tweet data.

    Args:
        tweet_data_list (list): A list of dictionaries containing tweet data.

    Returns:
        str: A review string generated from the tweet data.
    """
    review = ""
    for tweet in tweet_data_list:
        review += (f'Tweet by {tweet["displayName"]} (@{tweet["username"]}) on '
                   f'{tweet["date"]}:\n{tweet["rawContent"]}\n')
    return review[:2000]


def save_analysis(analysis: str, filename: str) -> None:
    """
    Saves the analysis to a markdown file, ensuring no file overwrite.

    Args:
        analysis (str): The analysis content to be saved.
        filename (str): The name of the file to save the analysis in.

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
