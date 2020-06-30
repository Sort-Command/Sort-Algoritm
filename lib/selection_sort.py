from lib.abstract_strategy import SortAlgorithm


class SelectionSort(SortAlgorithm):

    def __init__(self, target_list: list):
        super().__init__(target_list)

    def sort(self) -> None:
        n = len(self._target_list)
        for i in range(n):
            minimum = i

            for j in range(i + 1, n):
                if self._target_list[j] < self._target_list[minimum]:
                    minimum = j

            temp = self._target_list[i]
            self._target_list[i] = self._target_list[minimum]
            self._target_list[minimum] = temp

