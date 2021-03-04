# import get_heap
# get_heap.graphs_dir()
# from Shortest_paths.heap_dict import Heap, PriorQueue
from heap import PriorQueue

class MultiHeaps:

    def __init__(self, arr):  # high_heap, low_heap
        """
        Parameters:
        ----------
        high_heap  --  High min_heap
        low_heap  --  Low max_heap
        """
        self.low_heap = PriorQueue(arr[:len(arr) // 2], "max")
        self.high_heap = PriorQueue(arr[len(arr) // 2:], "min")
        self.multheap_property()

    def maintenance_size(self):
        """ Balance-function """
        high_heap = self.high_heap
        low_heap = self.low_heap
        while high_heap.heap_size >= low_heap.heap_size + 1:
            low_heap.max_heap_insert(high_heap.heap_extract_min())
        while low_heap.heap_size >= high_heap.heap_size + 1:
            high_heap.min_heap_insert(low_heap.heap_extract_max())

    def add_key(self, key):
        """
        1. insert new value to high_heap
        2. Balance heaps
        """
        self.high_heap.min_heap_insert(key)
        self.multheap_property()

    @property
    def size(self):
        self._size = len(self.high_heap.array) + len(self.low_heap.array)
        return self._size

    def multheap_property(self):
        high_heap = self.high_heap
        low_heap = self.low_heap
        while high_heap.array[0] < low_heap.array[0]:
            max_low = low_heap.heap_extract_max()
            high_heap.min_heap_insert(max_low)
            self.maintenance_size()

    @property
    def array(self):
        self._array = []
        self._array.extend(self.low_heap.array[::-1])
        self._array.extend(self.high_heap.array)
        return self._array



def median(multiheaps):
    """ Calc median with two heaps: High-min and Low-max. """
    if multiheaps.size % 2 == 0:
        m_ind = multiheaps.size // 2 - 1
    else:
        m_ind = (multiheaps.size + 1) // 2 - 1
    m = multiheaps.array[m_ind]
    return m

def median_loop(val_arr, multheaps):
    median_arr = []
    for i in range(len(val_arr) - 1):
        multheaps.add_key(val_arr[i])
        m = median(multiheaps)
        median_arr.append(m)
    return median_arr

arr = list(range(19))[::-1]
arr = MultiHeaps(arr)
med = median(arr)
print(med)