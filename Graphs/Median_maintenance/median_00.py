# import get_heap
# get_heap.graphs_dir()
# from Shortest_paths.heap_dict import Heap, PriorQueue
from heap import PriorQueue

a = PriorQueue()

class BalanceHeaps:

    def __init__(self, heap_1, heap_2):
        """
        Parameters:
        ----------
        heap_1  --  High min_heap
        heap_2  --  Low max_heap
        """
        self.heap_1 = heap_1
        self.heap_2 = heap_2

    def maintenance_size(self):
        """ Balance-function """
        heap_1 = self.heap_1
        heap_2 = self.heap_2
        while heap_1.heap_size >= heap_2.heap_size + 1:
            heap_2.max_heap_insert(heap_1.heap_extract_min())

    def add_key(self, key):
        # insert new value to heap_1
        self.heap_1.min_heap_insert(key)
        # Balance heaps
        self.maintenance_size()


# here will for-loop:
# 1. Add new value
# 2. Calc median and save it into array