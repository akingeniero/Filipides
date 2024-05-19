from project.conf.conf import user_dic, llm_dict
from project.ui.command_line.command_line_ui import CommandLineUi
from project.utils.singleton_meta import SingletonMeta
import logging


class Config(metaclass=SingletonMeta):

    def __init__(self):
        self.user_dic = user_dic
        self.llm_dict = llm_dict
        self.ui_managers = CommandLineUi()

    def get_user_config(self):
        return self.ui_managers.personal_user_select(self.user_dic)

    def get_llm_key(self):
        return self.llm_dict["openAI"]["key"]

    def get_llm_prompt(self):
        return self.ui_managers.prompt_select(self.llm_dict["openAI"]["prompts"])

    def get_llm_content(self):
        return self.llm_dict["openAI"]["content"]

