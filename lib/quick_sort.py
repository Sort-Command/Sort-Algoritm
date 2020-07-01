import random
from lib.abstract_strategy import SortAlgorithm


class QuickSort(SortAlgorithm):

    def __init__(self, target_list: list):
        super().__init__(target_list)

    def sort(self):
        if len(self._target_list) <= 1:
            return self._target_list
        else:
            q = random.choice(self._target_list)
            l_arr = [x for x in self._target_list if x < q]
            m_arr = [q] * self._target_list.count(q)
            r_arr = [x for x in self._target_list if x > q]
            return l_arr + m_arr + r_arr, self._target_list.sort()

