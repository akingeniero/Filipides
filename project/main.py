import asyncio
import logging

from project.client.openai_client import OpenAIClient
from project.client.twitter_client import TwitterClient
from project.ui.command_line.command_line_ui import CommandLineUi
from project.utils.config import Config
from project.utils.utils import fetch_and_analyze_tweets

logging.basicConfig(filename='project.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)


async def main() -> None:
    """
    Main function to run the program.

    Initializes clients, registers the Twitter client, selects a user, and performs tweet fetching and analysis.
    """
    logger.info("Program started")
    twitter_client = TwitterClient()
    await twitter_client.register()
    openai_client = OpenAIClient()
    user_id = ui_manager.target_user_select()
    await fetch_and_analyze_tweets(twitter_client, openai_client, user_id)
    logger.info("Program ended")


if __name__ == "__main__":
    """
    Entry point of the program. Initializes UI and configuration managers and runs the main async function.
    """
    ui_manager = CommandLineUi()
    config_manager = Config()
    asyncio.run(main())
