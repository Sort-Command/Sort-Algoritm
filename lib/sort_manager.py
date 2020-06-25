from lib.abstract_strategy import SortAlgorithm


class SortManager(object):

    def __init__(self, algorithm: SortAlgorithm):
        self._algorithm = algorithm

    def execute(self):
        self._algorithm.sort()
