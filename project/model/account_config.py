import configparser

class AccountConfig:
    """
    AccountConfig manages account-specific configuration settings.

    Attributes:
        config (configparser.ConfigParser): The configuration parser instance.
        section (str): The section in the configuration file containing account settings.
    """

    def __init__(self, config: configparser.ConfigParser, section: str):
        """
        Initializes the AccountConfig with the given configuration parser and section.

        Args:
            config (configparser.ConfigParser): The configuration parser instance.
            section (str): The section in the configuration file containing account settings.
        """
        self.config = config
        self.section = section

    def get_username(self) -> str:
        """
        Retrieves the username from the configuration.

        Returns:
            str: The username.
        """
        return self.config.get(self.section, 'username')

    def get_password(self) -> str:
        """
        Retrieves the password from the configuration.

        Returns:
            str: The password.
        """
        return self.config.get(self.section, 'password')

    def get_email(self) -> str:
        """
        Retrieves the email from the configuration.

        Returns:
            str: The email.
        """
        return self.config.get(self.section, 'email')

    def get_account_password(self) -> str:
        """
        Retrieves the account password from the configuration.

        Returns:
            str: The account password.
        """
        return self.config.get(self.section, 'account_password')