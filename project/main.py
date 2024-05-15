import asyncio

import twscrape

from project.client.openai_client import OpenAIClient
from project.client.twitter_client import TwitterClient
from project.config.configuration_manager import ConfigurationManager
from project.twitter.twitter_analyzer import TweetAnalyzer
from project.ui.command_line.command_line_ui import CommandLineUi


async def main():
    """
    Asynchronous main function that sets up and runs tweet analysis.

    This function reads the configuration, initializes the required instances,
    and performs tweet analysis for a specific user.

    Args:
        None

    Returns:
        None
    """
    config = ConfigurationManager.read_config('project/config/recourses/config.properties')
    ui_manager = CommandLineUi()
    await ConfigurationManager.add_user_config(ui_manager, config)
    llm_clas = ConfigurationManager.add_llm_config(ui_manager, config)
    twitter_client = TwitterClient(twscrape.API())
    openai_client = OpenAIClient(llm_clas, ui_manager)
    tweet_analyzer = TweetAnalyzer(twitter_client, openai_client)
    user_id = ui_manager.user_select()
    await tweet_analyzer.fetch_and_analyze_tweets(user_id)


if __name__ == "__main__":
    asyncio.run(main())
