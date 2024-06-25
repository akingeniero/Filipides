from array import array

from project.ui.command_line.command_line_ui import CommandLineUi
from project.ui.tkinter.tkinter_ui import TkinterUi
from project.utils.singleton_meta import SingletonMeta


class UiManager(metaclass=SingletonMeta):
    """
    Manager class to handle user interface interactions, supporting both command-line and Tkinter interfaces.
    """

    def __init__(self):
        """
        Initializes the UiManager with the necessary configurations.
        """
        self.ui_instance = None

    def setup_command_line_ui(self):
        """
        Sets up the command-line user interface.
        """
        self.ui_instance = CommandLineUi()

    def setup_tkinter_ui(self):
        """
        Sets up the Tkinter user interface.
        """
        self.ui_instance = TkinterUi()

    def mode_select(self) -> str:
        """
        Allows the user to select a mode (Twitter or News) through the current UI instance.

        Returns:
            str: Selected mode.
        """
        return self.ui_instance.mode_select()

    def personal_user_select(self, users: dict) -> dict:
        """
        Allows the user to select a personal user from a provided dictionary of users through the current UI instance.

        Args:
            users (dict): Dictionary of users where keys are user IDs and values are user details.

        Returns:
            dict: Selected user's details.
        """
        return self.ui_instance.personal_user_select(users)

    def prompt_select(self, prompts: dict) -> str:
        """
        Allows the user to select a prompt from a provided dictionary of prompts through the current UI instance.

        Args:
            prompts (dict): Dictionary of available prompts.

        Returns:
            str: Selected prompt.
        """
        return self.ui_instance.prompt_select(prompts)

    def target_user_select(self) -> int:
        """
        Allows the user to enter a target user's ID through the current UI instance.

        Returns:
            int: Selected target user's ID.
        """
        return self.ui_instance.target_user_select()

    def target_url_select(self) -> str:
        """
        Allows the user to enter a target URL through the current UI instance.

        Returns:
            str: Selected target URL.
        """
        return self.ui_instance.target_url_select()

    def continue_select(self) -> str:
        """
        Asks the user if they want to perform another operation through the current UI instance.

        Returns:
            str: The user's response in lowercase ('y' or 'n').
        """
        return self.ui_instance.continue_select()

    def error(self, error_text: str):
        """
        Displays an error message through the current UI instance.

        Args:
            error_text (str): The error message to display.

        Returns:
            None
        """
        self.ui_instance.error(error_text)

    def model_select(self, model: array) -> str:
        """
        Allows the user to select a model from a given list of models through the current UI instance.

        Args:
            model (array): List of available models.

        Returns:
            str: Selected model.
        """
        return self.ui_instance.model_select(model)

    def technology_select(self) -> str:
        """
        Allows the user to select a technology (OpenAI or Llama).

        Returns:
            str: Selected technology ('OpenAI' or 'Llama').
        """
        return self.ui_instance.technology_select()

