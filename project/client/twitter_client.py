import logging
from asyncio import sleep

from twscrape import gather, API

from project.utils.config import Config
from project.utils.singleton_meta import SingletonMeta

logger = logging.getLogger(__name__)


class TwitterClient(metaclass=SingletonMeta):
    """
    Client to interact with the Twitter API using twscrape.

    Attributes:
        api (API): The API client for interacting with Twitter.
        config (Config): Configuration object to fetch API keys and settings.
        users (dict): Dictionary containing user account information.
    """

    def __init__(self: 'TwitterClient') -> None:
        """
        Initializes the OpenAIClient with the necessary configurations.
        """
        self.api: API = API()
        self.config: Config = Config()
        logger.info("TwitterClient initialized")
        self.users: dict = {}

    async def register(self: 'TwitterClient') -> bool:
        """
        Registers the user accounts for the Twitter API.

        Args:
            self: Instance of TwitterClient.

        Returns:
            bool: True if registration is successful, False otherwise.
        """
        self.users: dict = self.config.get_user_config()
        await self.api.pool.add_account(self.users["username"], self.users["password"], self.users["email"],
                                        self.users["account_password"])
        user = await self.api.pool.login_all()
        if user["failed"] == 1:
            logger.error("Failed to register user")
            return False
        else:
            logger.info("User registered")
            await sleep(0.1)
            return True

    async def get_user_tweets(self: 'TwitterClient', user_id: int, limit: int = 20):
        """
        Retrieves tweets for a given user ID up to the specified limit.

        Args:
            self: Instance of TwitterClient.
            user_id (int): The user ID to fetch tweets for.
            limit (int): The maximum number of tweets to retrieve. Default is 20.

        Returns:
            list: A list of tweets for the specified user.
        """
        await self.api.user_by_id(user_id)
        logger.info(f"Extract tweets of: {user_id}")
        return gather(self.api.user_tweets(user_id, limit=limit))

    async def close(self):
        """
        Closes the TwitterClient and deletes the registered user accounts.

        Args:
            self: Instance of TwitterClient.

        Returns:
            None
        """
        await self.api.pool.delete_accounts(self.users["username"])
        pass
