import logging

from twscrape import gather, API

from project.utils.config import Config

logger = logging.getLogger(__name__)


class TwitterClient:

    def __init__(self):
        self.api = API()
        self.config = Config()
        logger.info("TwitterClient initialized")

    async def register(self):
        users = self.config.get_user_config()
        await self.api.pool.add_account(users["username"], users["password"], users["email"], users["account_password"])
        await self.api.pool.login_all()

    async def get_user_tweets(self, user_id, limit=20):
        await self.api.user_by_id(user_id)
        logger.info(f"Extract tweets of: {user_id}")
        return gather(self.api.user_tweets(user_id, limit=limit))
