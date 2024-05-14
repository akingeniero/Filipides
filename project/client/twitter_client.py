from twscrape import gather

class TwitterClient:
    """
    TwitterClient provides methods to interact with the Twitter API for fetching user tweets.

    Attributes:
        api (API): An instance of the Twitter API client.
    """

    def __init__(self, api):
        """
        Initializes the TwitterClient with the given API client.

        Args:
            api (API): An instance of the Twitter API client.
        """
        self.api = api

    def get_user_tweets(self, user_id, limit=20):
        """
        Fetches tweets for a given user.

        Args:
            user_id (int): The ID of the user whose tweets are to be fetched.
            limit (int, optional): The maximum number of tweets to fetch. Defaults to 20.

        Returns:
            list: A list of tweets fetched for the specified user.
        """
        self.api.user_by_id(user_id)
        return gather(self.api.user_tweets(user_id, limit=limit))
