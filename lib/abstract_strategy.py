from abc import ABC, abstractmethod


class SortAlgorithm(ABC):

    def __init__(self, target_list: list):
        self._target_list = target_list

    @abstractmethod
    def sort(self) -> None:
        pass
