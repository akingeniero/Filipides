import asyncio
import twscrape
from twscrape import gather

async def main():
    api = twscrape.API()

    user_id = 68740712
    await api.user_by_id(user_id)
    tweets = await gather(api.user_tweets(user_id, limit=20))

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

if __name__ == "__main__":
    asyncio.run(main())