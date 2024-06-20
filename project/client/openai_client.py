from openai import OpenAI
from project.ui.ui_manager import UiManager
from project.utils.config import Config
import logging
from project.utils.singleton_meta import SingletonMeta

logger = logging.getLogger(__name__)


class OpenAIClient(metaclass=SingletonMeta):
    """
    Client to interact with the OpenAI API.

    Attributes:
        config (Config): Configuration object to fetch API keys and settings.
        client (OpenAI): OpenAI client initialized with the API key.
        content (str): System content to guide the OpenAI model.
    """

    def __init__(self) -> None:
        """
        Initializes the OpenAIClient with the necessary configurations.
        """
        self.ui_managers = UiManager()
        self.config = Config()
        self.client = OpenAI(api_key=self.config.get_openai_key())
        self.content = self.config.get_openai_content()
        logger.info("OpenAIClient initialized")

    def _generate_response(self, prompt: str, placeholder: str, text: str) -> str:
        """
        Generates a response using OpenAI API by replacing a placeholder in the prompt with the given text.

        Args:
            prompt (str): The base prompt template.
            placeholder (str): The placeholder text to be replaced.
            text (str): The text to insert into the placeholder.

        Returns:
            str: The generated response.
        """
        final_prompt = prompt.replace(placeholder, text)
        logger.info(f"Generating text with prompt: {final_prompt}")

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": self.content},
                    {"role": "user", "content": final_prompt}
                ],
                temperature=0.5,
                max_tokens=1000
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "An error occurred while generating the response."

    def analyze_tweets(self, review: str) -> str:
        """
        Analyzes the given tweet review by generating a response from the OpenAI API.

        Args:
            review (str): The tweet review to be analyzed.

        Returns:
            str: The response generated by the OpenAI model.
        """
        return self._generate_response(self.config.get_openai_prompt("tweet"), "{text_tweet}", review)

    def analyze_news(self, review: str) -> str:
        """
        Analyzes the given news review by generating a response from the OpenAI API.

        Args:
            review (str): The news review to be analyzed.

        Returns:
            str: The response generated by the OpenAI model.
        """
        return self._generate_response(self.config.get_openai_prompt("notice"), "{text_new}", review)

    def verify_api_key(self) -> bool:
        """
        Verifies if the provided API key for OpenAI is valid.

        Returns:
            bool: True if the API key is valid, False otherwise.
        """
        try:
            self.client.models.list()
        except:
            return False
        else:
            return True
