from project.ui.command_line.command_line_ui import CommandLineUi
from project.ui.tkinter.tkinter_ui import TkinterUi
from project.utils.singleton_meta import SingletonMeta


class UiManager(metaclass=SingletonMeta):
    def __init__(self):
        self.ui_instance = None

    def setup_command_line_ui(self):
        self.ui_instance = CommandLineUi()

    def setup_tkinter_ui(self):
        self.ui_instance = TkinterUi()

    def mode_select(self) -> str:
        return self.ui_instance.mode_select()

    def personal_user_select(self, users: dict) -> dict:
        return self.ui_instance.personal_user_select(users)

    def prompt_select(self, prompts: dict) -> str:
        return self.ui_instance.prompt_select(prompts)

    def target_user_select(self) -> int:
        return self.ui_instance.target_user_select()

    def target_url_select(self) -> str:
        return self.ui_instance.target_url_select()

    def continue_select(self) -> str:
        return self.ui_instance.continue_select()

    def error(self, error_text: str):
        self.ui_instance.error(error_text)
