from lib.sort_manager import SortManager
from lib.bubble_sort import BubbleSort
from random import randint


if __name__ == '__main__':

    target_list1 = [randint(10, 99)for k in range(20)]
    selected_alg = BubbleSort(target_list1)
    sort_manager = SortManager(selected_alg)
    sort_manager.execute()
    print(target_list1)

    target_list2 = [randint(10, 999)for k in range(20)]
    selected_alg = SelectionSort(target_list2)
    sort_manager = SortManager(selected_alg)
    sort_manager.execute()
    print(target_list2)
