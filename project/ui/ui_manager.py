import abc
import configparser


class UiManager(abc.ABC):
    """
    Abstract base class for UI management. Defines the interface for
    interacting with the user interface, handling configuration, and
    saving settings.

    Methods:
        user_select_section(config: configparser.ConfigParser) -> str:
            Allows the user to select a section from the configuration.

        section_not_found():
            Handles the case when a section is not found in the configuration.

        user_initial_configuration():
            Handles the initial configuration process for the user.

        user_save():
            Saves the user-specific configuration.

        api_save():
            Saves the API-specific configuration.

        api_initial_configuration():
            Handles the initial configuration process for the API.
    """

    @abc.abstractmethod
    def user_select_section(self, config: configparser.ConfigParser) -> str:
        """
        Allows the user to select a section from the configuration.

        Args:
            config (configparser.ConfigParser): The configuration parser
            instance containing all sections and options.

        Returns:
            str: The name of the selected section.
        """
        pass

    @abc.abstractmethod
    def section_not_found(self):
        """
        Handles the case when a section is not found in the configuration.

        This method should inform the user that the requested section is
        not available.
        """
        pass

    @abc.abstractmethod
    def user_initial_configuration(self):
        """
        Handles the initial configuration process for the user.

        This method should guide the user through setting up their initial
        configuration options.
        """
        pass

    @abc.abstractmethod
    def user_save(self):
        """
        Saves the user-specific configuration.

        This method should handle saving any changes made to the user's
        configuration settings.
        """
        pass

    @abc.abstractmethod
    def api_save(self):
        """
        Saves the API-specific configuration.

        This method should handle saving any changes made to the API
        configuration settings.
        """
        pass

    @abc.abstractmethod
    def api_initial_configuration(self):
        """
        Handles the initial configuration process for the API.

        This method should guide the user through setting up the initial
        configuration options for the API.
        """
        pass
