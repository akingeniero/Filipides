import asyncio
import logging

from project.client.llm_client.llm_manager import LlmManager
from project.client.news_client import NewsClient
from project.client.twitter_client import TwitterClient
from project.ui.ui_manager import UiManager
from project.utils.config import Config
from project.utils.utils import fetch_and_analyze_tweets, fetch_and_analyze_news, load_report_from_file, analyze_llm

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
    global use_twitter
    use_twitter = False

    while True:
        environment_selection = ui_manager.environment_select()
        if environment_selection == 'Local':
            file_path = ui_manager.file_select()
            data_report = load_report_from_file(file_path)
            if data_report:
                tech = ui_manager.technology_select()
                await analyze_llm(tech, data_report, ui_manager)
            else:
                ui_manager.error("Invalid report file.")
        else:
            mode_selection = ui_manager.mode_select()
            if mode_selection == 'Twitter':
                use_twitter = True
                register_status = await twitter_client.register()
                if register_status:
                    user_id = ui_manager.target_user_select()
                    await fetch_and_analyze_tweets(user_id, ui_manager)
                else:
                    ui_manager.error("Failed to register user")
            elif mode_selection == 'News':
                url = ui_manager.target_url_select()
                await fetch_and_analyze_news(url, ui_manager)

        logger.info("Operation completed")

        continue_choice = ui_manager.continue_select()
        if continue_choice != 'y':
            if use_twitter:
                await twitter_client.close()
            break

    logger.info("Program ended")


if __name__ == "__main__":
    """
    Entry point of the program. Initializes UI and configuration managers and runs the main async function.
    """
    ui_manager = UiManager()
    llm_manager = LlmManager()
    ui_manager.setup_tkinter_ui()
    twitter_client = TwitterClient()
    news_client = NewsClient()
    config_manager = Config()
    asyncio.run(main())
