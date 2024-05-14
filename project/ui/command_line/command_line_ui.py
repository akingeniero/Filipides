import configparser

from project.ui.ui_manager import UiManager


class CommandLineUi(UiManager):
    def user_select_section(self, config: configparser.ConfigParser) -> str:
        print("Available sections:",
              ', '.join(section for section in config.sections() if section not in ["OpenAI", "DEFAULT"]))
        section = input("Enter the section to use for setup: ").strip()
        return section

    def section_not_found(self):
        print("Section not found")

    def user_initial_configuration(self):
        print("Initial user configuration Started")

    def user_save(self):
        print("User saved")

    def api_save(self):
        print("API saved")

    def api_initial_configuration(self):
        print("Initial api configuration Started")