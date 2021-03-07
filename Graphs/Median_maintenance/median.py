from heap import PriorQueue


class MultiHeaps:

    def __init__(self, arr):  # high_heap, low_heap
        """
        Empty array is not maintenance.
        Parameters:
        ----------
        high_heap  --  High min_heap
        low_heap  --  Low max_heap
        """
        if len(arr) > 1:
            self.low_heap = PriorQueue(arr[:len(arr) // 2], "max")
            self.high_heap = PriorQueue(arr[len(arr) // 2:], "min")
            self.multheap_property()
        else:  # if array is 1 element
            self.low_heap = PriorQueue(arr)
            self.high_heap = PriorQueue([])

    def maintenance_size(self):
        """ Balance-function """
        high_heap = self.high_heap
        low_heap = self.low_heap

        # Check case with 1 element
        if len(high_heap.array) > 0:
            # Check balanced or not sub-heaps
            while high_heap.heap_size >= low_heap.heap_size + 1:
                low_heap.max_heap_insert(high_heap.heap_extract_min())

            # use second bounder for control
            while low_heap.heap_size > high_heap.heap_size + 1:
                high_heap.min_heap_insert(low_heap.heap_extract_max())

    def add_key(self, key):
        """
        Addition new key to the MultiHeap-instance.
        """
        # insert new value to high_heap
        self.high_heap.min_heap_insert(key)

        # Balance heaps
        self.multheap_property()

    @property
    def size(self):
        """
        Get size of all array wich contains high_heap and low_heap.
        """
        self._size = len(self.high_heap.array) + len(self.low_heap.array)
        return self._size

    def multheap_property(self):
        """
        The func maintenance property of two balanced heap:
            one with half-largest and second with half-smallest elements.
        """
        high_heap = self.high_heap
        low_heap = self.low_heap
        if len(high_heap.array) > 0:
            while high_heap.array[0] < low_heap.array[0]:  # or high_heap.heap_size
                max_low = low_heap.heap_extract_max()
                high_heap.min_heap_insert(max_low)
                self.maintenance_size()
            self.maintenance_size()

    @property
    def array(self):
        """
        Get whole array for median search.
        """
        self._array = []
        self._array.extend(self.low_heap.array[::-1])
        self._array.extend(self.high_heap.array)
        return self._array


def median(multiheaps):
    """ Calc median with two heaps: High-min and Low-max. """
    if multiheaps.size == 1:
        return multiheaps.array[0]
    if multiheaps.size % 2 == 0:
        m_ind = multiheaps.size // 2 - 1
    else:
        m_ind = (multiheaps.size + 1) // 2 - 1
    m = multiheaps.array[m_ind]
    return m


def median_loop(val_arr:list):
    """
    Search all medians of sub-array of the given array.

    Parameters
    ----------
    val_arr : given array

    Returns
    -------
    array with all medians wich found.
    """
    multiheaps = MultiHeaps([val_arr[0]])  # MultiHeaps(PriorQueue([val_arr[0]]))
    median_arr = [val_arr[0]]
    for i in range(1, len(val_arr)):
        multiheaps.add_key(val_arr[i])
        m = median(multiheaps)
        median_arr.append(m)
    return median_arr


if __name__ == "__main__":
    # Pilot test-case:
    arr = list(range(19))[::-1]
    arr = MultiHeaps(arr)
    med = median(arr)
    print(med)

    # Test-cases from forum:
    arr = [1, 666, 10, 667, 100, 2, 3]
    medians1 = median_loop(arr)
    ans = sum(medians1) % 10000
    print(ans)

    data = open("Coursera_Algorithms_c2t3_Median.txt", "r")
    exam_cases = data.read().split('\n')
    exam_cases.pop()
    exam_cases = list(map(int, exam_cases))
    exam_medians = median_loop(exam_cases)
    answer = sum(exam_medians) % 10000
