from lib.abstract_strategy import SortAlgorithm


class BubbleSort(SortAlgorithm):

    def __init__(self, target_list: list):
        super().__init__(target_list)

    def sort(self) -> None:
        n = len(self._target_list)
        for i in range(n-1):
            for y in range(n - 1 - i):
                if self._target_list[i] < self._target_list[y+1]:
                    buffer = self._target_list[i]
                    self._target_list[i] = self._target_list[y+1]
                    self._target_list[y+1] = buffer
