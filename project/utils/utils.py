import os


async def fetch_and_analyze_tweets(twitter_client, openai_client, user_id: int) -> None:
    """
    Fetches tweets for a given user ID, processes the tweets, generates a review, and analyzes it using OpenAI.

    Args:
        twitter_client: An instance of the TwitterClient to fetch tweets.
        openai_client: An instance of the OpenAIClient to analyze tweets.
        user_id (str): The user ID to fetch tweets for.

    Returns:
        None
    """
    tweets = await twitter_client.get_user_tweets(user_id)
    tweet_data_list = await process_tweets(tweets)
    review = generate_review(tweet_data_list)
    analysis = openai_client.analyze_tweets(review)
    save_analysis(analysis, f"{user_id}.md")


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
