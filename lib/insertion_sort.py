from lib.abstract_strategy import SortAlgorithm


class InsertionSort(SortAlgorithm):

    def __init__(self, target_list: list):
        super().__init__(target_list)

    def sort(self) -> None:
        n = len(self._target_list)

        for i in range(n): #for i in range(n - 1): - will not sort the last element
            value_to_sort = self._target_list[i]

            while self._target_list[i - 1] > value_to_sort and i > 0:  # ...and i > 1 - wrong
                self._target_list[i], self._target_list[i - 1] = self._target_list[i - 1], self._target_list[i]
                i = i - 1


        return self._target_list #return list


# this section from "main.py":

# if __name__ == '__main__':
#
#     target_list = [randint(10, 99) for k in range(12)] # generator 'randint'
#     print(target_list)
#     select_algorithm = InsertionSort(target_list)
#
#     #select_algorithm = BubbleSort(target_list)
#
#     sort_manager = SortManager(select_algorithm)
#
#     sort_manager.execute() # run
#     print(target_list)








