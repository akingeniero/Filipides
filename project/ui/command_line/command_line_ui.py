import configparser
from project.ui.ui_manager import UiManager


class CommandLineUi(UiManager):
    """
    CommandLineUi is a concrete implementation of UiManager that interacts
    with the user through the command line interface.

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

    def user_select_section(self, config: configparser.ConfigParser) -> str:
        """
        Allows the user to select a section from the configuration.

        Args:
            config (configparser.ConfigParser): The configuration parser
            instance containing all sections and options.

        Returns:
            str: The name of the selected section.
        """
        print("Available sections:",
              ', '.join(section for section in config.sections() if section not in ["OpenAI", "DEFAULT"]))
        section = input("Enter the section to use for setup: ").strip()
        return section

    def section_not_found(self):
        """
        Handles the case when a section is not found in the configuration.

        This method informs the user that the requested section is not available.
        """
        print("Section not found")

    def user_initial_configuration(self):
        """
        Handles the initial configuration process for the user.

        This method guides the user through setting up their initial configuration options.
        """
        print("Initial user configuration Started")

    def user_save(self):
        """
        Saves the user-specific configuration.

        This method handles saving any changes made to the user's configuration settings.
        """
        print("User saved")

    def api_save(self):
        """
        Saves the API-specific configuration.

        This method handles saving any changes made to the API configuration settings.
        """
        print("API saved")

    def api_initial_configuration(self):
        """
        Handles the initial configuration process for the API.

        This method guides the user through setting up the initial configuration options for the API.
        """
        print("Initial api configuration Started")
