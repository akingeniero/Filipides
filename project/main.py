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
        if openai_client.verify_api_key():
            if mode_selection == 'Twitter':
                register_status = await twitter_client.register()
                if register_status:
                    user_id = ui_manager.target_user_select()
                    await fetch_and_analyze_tweets(user_id)
                else:
                    ui_manager.error("Failed to register user")
            elif mode_selection == 'News':
                url = ui_manager.target_url_select()
                if openai_client.verify_api_key():
                    await fetch_and_analyze_news(url)
        else:
            ui_manager.error("Invalid OpenAI API key")

        logger.info("Operation completed")

        continue_choice = ui_manager.continue_select()
        if continue_choice != 'y':
            await twitter_client.close()
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
