import configparser


class AccountConfig:

    def __init__(self, config: configparser.ConfigParser, section):
        self.config = config
        self.section = section

    def get_username(self) -> str:
        return self.config.get(self.section, 'username')

    def get_password(self) -> str:
        return self.config.get(self.section, 'password')

    def get_email(self) -> str:
        return self.config.get(self.section, 'email')

    def get_account_password(self) -> str:
        return self.config.get(self.section, 'account_password')
