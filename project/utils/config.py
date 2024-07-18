from project.conf.conf import user_dic, openai_dict, llama_dict, llm_dict
from project.ui.ui_manager import UiManager
from project.utils.singleton_meta import SingletonMeta
import logging

logger = logging.getLogger(__name__)


class Config(metaclass=SingletonMeta):
    """
    Configuration manager class that implements the singleton pattern to ensure a single instance.

    Attributes:
        user_dic (dict): Dictionary containing user configurations.
        openai_dict (dict): Dictionary containing OpenAI configurations.
        llama_dict (dict): Dictionary containing Llama configurations.
        llm_dict (dict): Dictionary containing general LLM configurations.
        ui_managers (UiManager): Instance of UiManager to handle user interface interactions.
    """

    def __init__(self) -> None:
        """
        Initializes the Config class with the necessary configurations.
        """
        self.user_dic: dict = user_dic
        self.openai_dict: dict = openai_dict
        self.llama_dict: dict = llama_dict
        self.llm_dict: dict = llm_dict
        self.ui_managers = UiManager()

    def get_user_config(self) -> dict:
        """
        Retrieves the user configuration by selecting a personal user through the UI manager.

        Returns:
            dict: Selected user's configuration.
        """
        return self.ui_managers.personal_user_select(self.user_dic)

    def get_openai_key(self) -> str:
        """
        Retrieves the API key for OpenAI.

        Returns:
            str: API key for OpenAI.
        """
        return self.openai_dict["openAI"]["key"]

    def get_llama_key(self) -> str:
        """
        Retrieves the API key for Llama.

        Returns:
            str: API key for Llama.
        """
        return self.llama_dict["llama"]["key"]

    def get_llm_prompt(self, type_prompt: str) -> str:
        """
        Retrieves the prompt for the language model by selecting through the UI manager.

        Args:
            type_prompt (str): The type of prompt to retrieve.

        Returns:
            str: Selected prompt.
        """
        return self.ui_managers.prompt_select(self.llm_dict["prompts"][type_prompt])

    def get_llm_system_context(self) -> str:
        """
        Retrieves the system context for the language model.

        Returns:
            str: System context for the language model.
        """
        return self.llm_dict["content"]

    def get_openai_llm(self) -> str:
        """
        Retrieves the OpenAI language model by selecting through the UI manager.

        Returns:
            str: Selected OpenAI model.
        """
        return self.ui_managers.model_select(self.openai_dict["openAI"]["llms"])

    def get_llama_llm(self) -> str:
        """
        Retrieves the Llama language model by selecting through the UI manager.

        Returns:
            str: Selected Llama model.
        """
        return self.ui_managers.model_select(self.llama_dict["llama"]["llms"])
