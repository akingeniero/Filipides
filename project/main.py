import asyncio
import logging

from project.client.news_client import NewsClient
from project.client.openai_client import OpenAIClient
from project.client.twitter_client import TwitterClient
from project.ui.command_line.command_line_ui import CommandLineUi
from project.utils.config import Config
from project.utils.utils import fetch_and_analyze_tweets, fetch_and_analyze_news

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
    while True:
        mode_selection = ui_manager.mode_select()

        if mode_selection == 'Twitter':
            await twitter_client.register()
            user_id = ui_manager.target_user_select()
            await fetch_and_analyze_tweets(user_id)
        elif mode_selection == 'News':
            url = ui_manager.target_url_select()
            await fetch_and_analyze_news(url)

        logger.info("Operation completed")

        continue_choice = ui_manager.continue_select()
        if continue_choice != 'y':
            break

    logger.info("Program ended")


if __name__ == "__main__":
    """
    Entry point of the program. Initializes UI and configuration managers and runs the main async function.
    """
    ui_manager = CommandLineUi()
    twitter_client = TwitterClient()
    news_client = NewsClient()
    config_manager = Config()
    openai_client = OpenAIClient()

    asyncio.run(main())
