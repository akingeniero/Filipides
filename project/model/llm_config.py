import configparser
import json


class LlmConfig:

    def __init__(self, config: configparser.ConfigParser, section):
        self.config = config
        self.section = section

    def get_api_key(self) -> str:
        return self.config.get(self.section, 'key')

    def get_prompts(self) -> dict:
        prompts_str = self.config.get(self.section, 'prompts')
        prompts_dict = json.loads(prompts_str)
        return prompts_dict
