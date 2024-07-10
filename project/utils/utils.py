import json
import os
from datetime import datetime

from project.client.llm_client.llm_manager import LlmManager
from project.client.news_client import NewsClient
from project.client.twitter_client import TwitterClient
from project.ui.ui_manager import UiManager


def select_tech(tech, llm_manager):
    """
    Sets up the appropriate LLM client based on the selected technology.

    Args:
        tech (str): The selected technology ('OpenAI' or 'Llama').
        llm_manager (LlmManager): The LLM manager instance.
    """
    if tech == 'OpenAI':
        llm_manager.setup_openai_client()
        llm_manager.verify_api_key()
    else:
        llm_manager.setup_llama_client()


def load_report_from_file(file_path):
    """
    Loads and validates the report JSON from a local file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Loaded report dictionary if valid, None otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            report = json.load(file)

        if 'type' not in report:
            print("Invalid report structure. Missing 'type' key.")
            return None

        if report["type"] == "tweet" and all(key in report for key in ("user_id", "review", "timestamp")):
            return report
        elif report["type"] == "news" and all(key in report for key in ("url", "review", "timestamp")):
            return report
        else:
            print("Invalid report structure. Missing required keys.")
            return None

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {str(e)}")
        return None


async def fetch_and_analyze_tweets(user_id: int, ui_manager: UiManager) -> None:
    """
    Fetches tweets for a given user ID, processes the tweets, generates a review, and analyzes it using the selected LLM.

    Args:
        user_id (int): The user ID to fetch tweets for.
        ui_manager (UiManager): The UI manager instance.

    Returns:
        None
    """
    twitter_client = TwitterClient()
    tweets = await twitter_client.get_user_tweets(user_id)
    tweet_data_list = await process_tweets(tweets)
    review = generate_review(tweet_data_list)
    tweet_report = {
        "type": "tweet",
        "user_id": user_id,
        "review": review,
        "timestamp": datetime.now().isoformat()
    }
    tweet_report_str = json.dumps(tweet_report, indent=4, ensure_ascii=False)
    save_analysis(tweet_report_str, f"tweet_report_{user_id}.json", ui_manager, "./tweets_reports")
    tech = ui_manager.technology_select()
    await analyze_llm(tech, tweet_report, ui_manager)


async def fetch_and_analyze_news(url_news: str, ui_manager: UiManager) -> None:
    """
    Fetches the main news content from a given URL, generates a review, and analyzes it using the selected LLM.

    Args:
        url_news (str): The URL of the news article to analyze.
        ui_manager (UiManager): The UI manager instance.

    Returns:
        None
    """
    news_client = NewsClient()
    news = await news_client.extract_main_news(url_news)
    title_name = news[8:28]
    review = news[:2000]
    news_report = {
        "type": "news",
        "url": url_news,
        "review": review,
        "timestamp": datetime.now().isoformat()
    }
    news_report_str = json.dumps(news_report, indent=4, ensure_ascii=False)
    save_analysis(news_report_str, f"news_report_{title_name}.json",  ui_manager, "./news_reports")
    tech = ui_manager.technology_select()
    await analyze_llm(tech, news_report, ui_manager)


async def analyze_llm(tech, report, ui_manager: UiManager):
    """
    Analyzes the provided report using the selected LLM technology.

    Args:
        tech (str): The selected technology ('OpenAI' or 'Llama').
        report (dict): The report to analyze.
        ui_manager (UiManager): The UI manager instance.

    Returns:
        None
    """
    llm_manager = LlmManager()
    select_tech(tech, llm_manager)
    review = report["review"]
    report_type = report["type"]
    data_type_raw = report["url"] if report_type == "news" else report["user_id"]

    if report_type == "news":
        analysis, elapsed_time = llm_manager.analyze_news(review)
        analysis_report = {
            "type": report_type,
            "tech": tech,
            "review": review,
            "analysis": analysis,
            "elapsed_time": elapsed_time,
            "timestamp": datetime.now().isoformat(),
            "url_new": data_type_raw
        }
        title_report = review[8:20]
        directory_report = "./news_analysis_reports"
    else:
        analysis, elapsed_time = llm_manager.analyze_tweets(review)
        analysis_report = {
            "type": report_type,
            "tech": tech,
            "review": review,
            "analysis": analysis,
            "elapsed_time": elapsed_time,
            "timestamp": datetime.now().isoformat(),
            "userid": data_type_raw
        }
        title_report = data_type_raw
        directory_report = "./tweets_analysis_reports"

    analysis_report_str = json.dumps(analysis_report, indent=4, ensure_ascii=False)
    save_analysis(analysis_report_str, f"analysis_report_{title_report}.json", ui_manager, directory_report)


async def process_tweets(tweets_coroutine) -> list:
    """
    Processes tweets by extracting relevant information into a structured format.

    Args:
        tweets_coroutine: Coroutine that fetches tweets.

    Returns:
        list: A list of dictionaries containing tweet data.
    """
    tweet_data_list = []
    tweets = await tweets_coroutine
    for tweet in tweets:
        tweet_data = {
            "id": tweet.id_str,
            "url": tweet.url,
            "date": tweet.date,
            "username": tweet.user.username,
            "displayName": tweet.user.displayname,
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
    return tweet_data_list


def generate_review(tweet_data_list: list) -> str:
    """
    Generates a review string from a list of tweet data.

    Args:
        tweet_data_list (list): A list of dictionaries containing tweet data.

    Returns:
        str: A review string generated from the tweet data.
    """
    review = ""
    for tweet in tweet_data_list:
        review += (f'Tweet by {tweet["displayName"]} (@{tweet["username"]}) on '
                   f'{tweet["date"]}:\n{tweet["rawContent"]}\n')
    return review[:2000]


def save_analysis(analysis: str, filename: str, ui_manager: UiManager, directory: str = '.') -> None:
    """
    Saves the analysis to a JSON file, ensuring no file overwrite.

    Args:
        analysis (str): The analysis content to be saved.
        filename (str): The name of the file to save the analysis in.
        ui_manager (UiManager): The UI manager instance.
        directory (str, optional): The directory where the file should be saved. Defaults to current directory ('.').

    Returns:
        None
    """
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(file_path):
            file_path = os.path.join(directory, f"{base}_{counter}{ext}")
            counter += 1

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(analysis.strip())

    ui_manager.show_report(filename)
