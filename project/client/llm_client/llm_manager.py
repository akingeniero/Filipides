from typing import Any

from project.client.llm_client.llama_client.llama_client import LlamaClient
from project.client.llm_client.openai_client.openai_client import OpenAIClient
from project.utils.singleton_meta import SingletonMeta
from project.utils.config import Config
import logging

logger = logging.getLogger(__name__)


class LlmManager(metaclass=SingletonMeta):
    """
    Manager class to handle user interface interactions, supporting both openai and llama.
    """

    def __init__(self):
        """
        Initializes the LlmManager with the necessary configurations.
        """
        self.ui_instance = None
        self.config = Config()

    def setup_openai_client(self):
        """
        Sets up the OpenAI client.
        """
        self.ui_instance = OpenAIClient()

    def setup_llama_client(self):
        """
        Sets up the Llama client.
        """
        self.ui_instance = LlamaClient()

    def analyze_tweets(self, text: str) -> tuple[Any, float]:
        """
        Analyzes the given tweet review by generating a response from the Llama API.

        Args:
            text (str): The tweet to analyze.

        Returns:
            str: The analysis result.
        """
        return self.ui_instance.analyze_tweets(text)

    def analyze_news(self, text: str) -> str:
        """
        Analyzes the given tweet review by generating a response from the Llama API.

        Args:
            text (str): The tweet to analyze.

        Returns:
            str: The analysis result.
        """
        return self.ui_instance.analyze_news(text)

    def verify_api_key(self) -> bool:
        """
        Verifies the LLm API key if the current instance is OpenAIClient.

        Returns:
            bool: True if the API key is valid, False otherwise.
        """
        return self.ui_instance.verify_api_key()