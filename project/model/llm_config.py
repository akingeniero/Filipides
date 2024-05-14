import configparser
import json

class LlmConfig:
    """
    LlmConfig manages the configuration settings for a language model.

    Attributes:
        config (configparser.ConfigParser): The configuration parser instance.
        section (str): The section in the configuration file containing LLM settings.
    """

    def __init__(self, config: configparser.ConfigParser, section: str):
        """
        Initializes the LlmConfig with the given configuration parser and section.

        Args:
            config (configparser.ConfigParser): The configuration parser instance.
            section (str): The section in the configuration file containing LLM settings.
        """
        self.config = config
        self.section = section

    def get_api_key(self) -> str:
        """
        Retrieves the API key from the configuration.

        Returns:
            str: The API key.
        """
        return self.config.get(self.section, 'key')

    def get_prompts(self) -> dict:
        """
        Retrieves the prompts from the configuration.

        Returns:
            dict: A dictionary of prompts.
        """
        prompts_str = self.config.get(self.section, 'prompts')
        prompts_dict = json.loads(prompts_str)
        return prompts_dict
