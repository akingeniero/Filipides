import abc

from project.utils.singleton_abc_meta import SingletonABCMeta


class UiManager(metaclass=SingletonABCMeta):

    @abc.abstractmethod
    def personal_user_select(self, users: dict) -> str:
        pass

    @abc.abstractmethod
    def prompt_select(self, prompts) -> str:
        pass

    @abc.abstractmethod
    def target_user_select(self) -> int:
        pass
