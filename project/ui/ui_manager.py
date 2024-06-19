import abc
from project.utils.singleton_abc_meta import SingletonABCMeta


class UiManager(metaclass=SingletonABCMeta):
    """
    Abstract base class for UI management. Ensures that only one instance
    of UiManager is created (singleton pattern) and enforces implementation
    of essential UI selection methods.

    Methods:
        personal_user_select(users: dict) -> dict:
            Abstract method to select a personal information user from a dictionary of users.

        prompt_select(prompts: list) -> str:
            Abstract method to select a prompt from a list of prompts.

        target_user_select() -> int:
            Abstract method to select a target user by returning their user ID.
    """

    @abc.abstractmethod
    def personal_user_select(self, users: dict) -> dict:
        """
        Selects a personal user from the given dictionary of users.

        Args:
            users (dict): Dictionary of users where keys are user IDs and values are user details.

        Returns:
            dict: Selected user's details.
        """
        pass

    @abc.abstractmethod
    def prompt_select(self, prompts: list) -> str:
        """
        Selects a prompt from the given list of prompts.

        Args:
            prompts (list): List of available prompts.

        Returns:
            str: Selected prompt.
        """
        pass

    @abc.abstractmethod
    def target_user_select(self) -> int:
        """
        Selects a target user and returns their user ID.

        Returns:
            int: Selected target user's ID.
        """
        pass

    @abc.abstractmethod
    def continue_select(self) -> int:
        """
        Selects a target user and returns their user ID.

        Returns:
            int: Selected target user's ID.
        """
        pass

    @abc.abstractmethod
    def target_url_select(self) -> int:
        """
        Selects a target user and returns their user ID.

        Returns:
            int: Selected target user's ID.
        """
        pass

    @abc.abstractmethod
    def target_url_select(self) -> int:
        """
        Selects a target user and returns their user ID.

        Returns:
            int: Selected target user's ID.
        """
        pass

    @abc.abstractmethod
    def mode_select(self) -> int:
        """
        Selects a target user and returns their user ID.

        Returns:
            int: Selected target user's ID.
        """
        pass
