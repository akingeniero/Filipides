import os


async def fetch_and_analyze_tweets(twitter_client, openai_client, user_id):
    tweets = await twitter_client.get_user_tweets(user_id)
    tweet_data_list = await process_tweets(tweets)
    review = generate_review(tweet_data_list)
    analysis = openai_client.analyze_tweets(review)
    save_analysis(analysis, f"{user_id}.md")


async def process_tweets(tweets_coroutine):
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


def generate_review(tweet_data_list):
    review = ""
    for tweet in tweet_data_list:
        review += (f'Tweet by {tweet["displayName"]} (@{tweet["username"]}) on '
                   f'{tweet["date"]}:\n{tweet["rawContent"]}\n')
    return review[:2000]


def save_analysis(analysis, filename):
    file_path = filename
    if os.path.exists(file_path):
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(file_path):
            file_path = f"{base}_{counter}{ext}"
            counter += 1

    with open(file_path, 'w') as file:
        file.write(analysis.strip())
