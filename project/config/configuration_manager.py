import configparser

from twscrape import API

from project.model.account_config import AccountConfig
from project.model.llm import Llm
from project.model.llm_config import LlmConfig
from project.ui.ui_manager import UiManager


class ConfigurationManager:
    @staticmethod
    def read_config(config_path: str, encoding: str = 'ISO-8859-1') -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        with open(config_path, encoding=encoding) as config_file:
            config.read_file(config_file)
        return config
        pass

    def add_user_config(self: UiManager, config: configparser.ConfigParser):

        self.user_initial_configuration()
        section = self.user_select_section(config)
        while section not in config.sections():
            self.section_not_found()
            section = self.user_select_section(config)
        account_config = AccountConfig(config, section)

        api = API()

        api.pool.add_account(account_config.get_username(), account_config.get_password(),
                                       account_config.get_email(), account_config.get_account_password())
        api.pool.login_all()

        self.user_save()

    def add_llm_config(self: UiManager, config: configparser.ConfigParser) -> Llm:
        self.api_initial_configuration()
        openai_config = LlmConfig(config, "openAI")
        return Llm(openai_config.get_api_key(), openai_config.get_prompts())
