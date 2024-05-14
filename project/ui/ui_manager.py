import abc
import configparser


class UiManager(abc.ABC):
    @abc.abstractmethod
    def user_select_section(self, config: configparser.ConfigParser) -> str:
        pass

    @abc.abstractmethod
    def section_not_found(self):
        pass

    @abc.abstractmethod
    def user_initial_configuration(self):
        pass

    @abc.abstractmethod
    def user_save(self):
        pass

    @abc.abstractmethod
    def api_save(self):
        pass

    @abc.abstractmethod
    def api_initial_configuration(self):
        pass

