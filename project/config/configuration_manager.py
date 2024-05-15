import asyncio
import configparser
from twscrape import API
from project.model.account_config import AccountConfig
from project.model.llm import Llm
from project.model.llm_config import LlmConfig
from project.ui.ui_manager import UiManager


class ConfigurationManager:
    """
    ConfigurationManager provides methods to read configuration files and
    manage user and LLM configurations.

    Methods:
        read_config(config_path: str, encoding: str = 'ISO-8859-1') -> configparser.ConfigParser:
            Reads and parses a configuration file.

        add_user_config(self: UiManager, config: configparser.ConfigParser):
            Adds user-specific configuration and initializes the API.

        add_llm_config(self: UiManager, config: configparser.ConfigParser) -> Llm:
            Adds LLM-specific configuration and returns an Llm instance.
    """

    @staticmethod
    def read_config(config_path: str, encoding: str = 'ISO-8859-1') -> configparser.ConfigParser:
        """
        Reads and parses a configuration file.

        Args:
            config_path (str): The path to the configuration file.
            encoding (str): The encoding of the configuration file. Defaults to 'ISO-8859-1'.

        Returns:
            configparser.ConfigParser: The parsed configuration object.
        """
        config = configparser.ConfigParser()
        with open(config_path, encoding=encoding) as config_file:
            config.read_file(config_file)
        return config

    async def add_user_config(self: UiManager, config: configparser.ConfigParser):
        """
        Adds user-specific configuration and initializes the API.

        This method guides the user through the initial configuration process,
        selects the appropriate section from the configuration, and sets up
        the API with the user's account information.

        Args:
            self (UiManager): An instance of the UiManager interface.
            config (configparser.ConfigParser): The parsed configuration object.

        Returns:
            None
        """
        self.user_initial_configuration()
        section = self.user_select_section(config)
        while section not in config.sections():
            self.section_not_found()
            section = self.user_select_section(config)
        account_config = AccountConfig(config, section)

        api = API()

        await api.pool.add_account(account_config.get_username(), account_config.get_password(),
                             account_config.get_email(), account_config.get_account_password())
        await api.pool.login_all()

        self.user_save()

    def add_llm_config(self: UiManager, config: configparser.ConfigParser) -> Llm:
        """
        Adds LLM-specific configuration and returns an Llm instance.

        This method guides the user through the initial configuration process for the LLM
        and sets up the necessary configuration using the specified section from the configuration file.

        Args:
            self (UiManager): An instance of the UiManager interface.
            config (configparser.ConfigParser): The parsed configuration object.

        Returns:
            Llm: An instance of the Llm class with the configured API key and prompts.
        """
        self.api_initial_configuration()
        openai_config = LlmConfig(config, "openAI")
        return Llm(openai_config.get_api_key(), openai_config.get_prompts())
