from project.conf.conf import user_dic, llm_dict
from project.ui.command_line.command_line_ui import CommandLineUi
from project.utils.singleton_meta import SingletonMeta
import logging

logger = logging.getLogger(__name__)


class Config(metaclass=SingletonMeta):
    """
    Configuration manager class that implements the singleton pattern to ensure a single instance.

    Attributes:
        user_dic (dict): Dictionary containing user configuration.
        llm_dict (dict): Dictionary containing language model configuration.
        ui_managers (CommandLineUi): Instance of the command line UI manager.
    """

    def __init__(self: 'Config') -> None:
        """
        Initializes the Config class with user and language model dictionaries, and the command line UI manager.

        Args:
            self: Instance of Config.

        Returns:
            None
        """
        self.user_dic: dict = user_dic
        self.llm_dict: dict = llm_dict
        self.ui_managers: CommandLineUi = CommandLineUi()

    def get_user_config(self: 'Config') -> dict:
        """
        Retrieves the user configuration by selecting a personal user through the UI manager.

        Args:
            self: Instance of Config.

        Returns:
            str: Selected user's ID.
        """
        return self.ui_managers.personal_user_select(self.user_dic)

    def get_llm_key(self: 'Config') -> str:
        """
        Retrieves the API key for the language model.

        Args:
            self: Instance of Config.

        Returns:
            str: API key for the language model.
        """
        return self.llm_dict["openAI"]["key"]

    def get_llm_prompt(self: 'Config') -> str:
        """
        Retrieves the prompt for the language model by selecting through the UI manager.

        Args:
            self: Instance of Config.

        Returns:
            str: Selected prompt.
        """
        return self.ui_managers.prompt_select(self.llm_dict["openAI"]["prompts"])

    def get_llm_content(self: 'Config') -> str:
        """
        Retrieves the system content for the language model.

        Args:
            self: Instance of Config.

        Returns:
            str: System content for the language model.
        """
        return self.llm_dict["openAI"]["content"]
