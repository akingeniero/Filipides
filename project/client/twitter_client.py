from twscrape import gather


class TwitterClient:
    def __init__(self, api):
        self.api = api

    def get_user_tweets(self, user_id, limit=20):
        self.api.user_by_id(user_id)
        return gather(self.api.user_tweets(user_id, limit=limit))
