class Heap(object):
    """ For [*dict.items()] style -> list of tuples of pair values: (name_vertex, distance_to_vertex).
    distance_to_vertex : sum of weights of edges from source vertex to the vertex.
    """

    def __init__(self, array: dict, key=None):
        self.array = [*array.items()]
        self._hs = None
        if key == "min":
            self.build_min_heap()
        if key == "max":
            self.build_max_heap()

    @staticmethod
    def parent(i):
        """ In the case 'round' is analog ceil (for power of 2). """
        # if i % 2:
        #     return i // 2
        return (i - 1) // 2 #  round(i / 2)

    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

    @property
    def heap_size(self, array=None):
        if array is None:
            array = self.array
        # if self._hs == None:
        #     self.heap_size = len(self.array) - 1
        # return self._hs
        return len(array) - 1

    # @heap_size.setter
    # def heap_size(self, i):
    #     self._hs = i
    #     return self._hs


    def max_heapify(self, i, array=None):
        # A = Heap(dict(self.array)) # self.array  # self.Instance.heap_size(A)
        if array is None:
            array = self.array
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and array[l][1] > array[i][1]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and array[r][1] > array[largest][1]:
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.max_heapify(largest, array)

    def min_heapify(self, i, array=None):
        # A = Heap(self.array) # self.array # self.Instance.heap_size(A)
        if array is None:
            array = self.array
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and array[l][1] < array[i][1]:
            smallest = l
        else:
            smallest = i
        if r <= self.heap_size and array[r][1] < array[smallest][1]:
            smallest = r
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]
            self.min_heapify(smallest, array)

    def build_max_heap(self, array=None):
        # self.heap_size = len(self.array)
        if array is None:
            array = self.array
        for i in range(len(array)//2 - 1, -1, -1): # range(len(self.array)//2 - 1, -1, -1):
            self.max_heapify(i, array)

    def build_min_heap(self, array=None):
        if array is None:
            array = self.array
        for i in range(len(self.array)//2 - 1, -1, -1):  # reversed(range(len(self.array)//2)):
            self.min_heapify(i, array)



class PriorQueue(Heap):

    def heap_extract_max(self, array=None):
        if array is None:
            array = self.array
        if self.heap_size < 1:
            raise IndexError("The queue is empty.")
        max = array[0]
        array[0] = array[self.heap_size]
        # self.heap_size -= 1
        array.pop()
        self.max_heapify(0, array)
        return max
    
    def heap_extract_min(self, array=None):
        if array is None:
            array = self.array
        if self.heap_size < 1:
            raise IndexError("The queue is empty.")
        min = array[0]
        array[0] = array[self.heap_size]
        # self.heap_size -= 1
        array.pop()
        self.min_heapify(0, array)
        return min

    def heap_increase_key(self, i, key, array=None):
        if array is None:
            array = self.array
        if key < array[i][1]:
            raise ValueError("new key is smaller than current key")
        # self.array[i][1] = key
        elem = (array[i][0], key)
        array[i] = elem
        while i > 0 and array[self.parent(i)][1] < array[i][1]:
            array[i], array[self.parent(i)] = array[self.parent(i)], array[i]
            i = self.parent(i)

    def heap_decrease_key(self, i, key, array=None):
        if array is None:
            array = self.array
        if key > array[i][1]:
            raise ValueError("new key is larger than current key")
        # self.array = list(self.array)
        elem = (array[i][0], key)
        array[i] = elem
        while i > 0 and array[self.parent(i)][1] > array[i][1]:
            array[i], array[self.parent(i)] = array[self.parent(i)], array[i]
            i = self.parent(i)
        # self.array = tuple(self.array)

    def max_heap_insert(self, key, val, array=None):
        if array is None:
            array = self.array
        array.append((key, float('-inf')))
        # heap_size = len(self.array) - 1
        self.heap_increase_key(self.heap_size, val, array)

    def min_heap_insert(self, key, val, array=None):
        if array is None:
            array = self.array
        array.append((key, float('inf')))
        # heap_size = len(self.array) - 1
        self.heap_decrease_key(self.heap_size, val, array)


# def heapsort(array):
#     # from collections import deque
#     # array = cls.array
#     # sort_arr = deque([])
#     # build_max_heap()
#     # for i in range(cls.heap_size, 0, -1):
#     #     cls.array[0], cls.array[i] = cls.array[i], cls.array[0]
#     #     sort_arr.appendleft(cls.array[i])
#     #     cls.array.pop()
#     #     cls
#     build_max_heap()
#     for i in range(len(array), 0, -1):
#         array[0], array[i] = array[i], array[0]


def T(arr):
    return [i[1] for i in arr]


if __name__ == "__main__":
    A = dict(zip(["a", "b", "c", "d", "e"], [10, 50, 3, 8, 2]))
    A = Heap(A, "max")
    print("Test 1.1: Build-Max-Heap", T(A.array))
    A = Heap(dict(A.array), "min")
    print("Test 1.2: Build-Min-Heap", T(A.array))


    a2 = dict(zip(["A", "B", "C", "D", "E", "F", "G"], [500, 400, 200, 100, 150, 1, 10]))
    a2 = Heap(a2, "max")
    # a2.build_max_heap()
    print("Test 2.1: Build-Max-Heap", T(a2.array))
    a2.build_min_heap()
    print("Test 2.2: Build-Min-Heap", T(a2.array))

    B = zip(["a", "b", "c", "d", "e"], [10, 50, 3, 8, 2])
    B = PriorQueue(dict(B))
    B.build_min_heap()
    print("Test 3.1: Build-Min-Heap", "\tB-heap:\n", T(B.array))
    print("extracted min =", B.heap_extract_min())
    print("array after extracted:", T(B.array))
    B.min_heap_insert("min_insert", 1)
    print("after insertion 1 to heap B:", T(B.array))
    B.min_heap_insert("min_insert", 4)
    print("after insertion 4 to heap B:", T(B.array))

    b2 = zip(["A", "B", "C", "D", "E", "F", "G"], [500, 400, 200, 100, 150, 1, 10])
    b2 = PriorQueue(dict(b2))
    b2.build_min_heap()
    print("Test 4.1: Build-Min-Heap", "\tb2-heap:\n", T(b2.array))
    print("extracted min =", b2.heap_extract_min())
    print("array after extracted:", T(b2.array))
    b2.min_heap_insert("max_insert", 600)
    print("after insertion 600 to heap b2:", T(b2.array))
    b2.build_max_heap()
    print("Max-Heap:", T(b2.array))
    b2.max_heap_insert("Max-Heap_insert", 700)
    print(f"After insert {700}:", T(b2.array))
    b2.build_min_heap()
    print("Min-Heap:", T(b2.array))
    b2.min_heap_insert("min_insert", 0.5)
    print(f"After insert {0.5}:", T(b2.array))
    b2.min_heap_insert("round", 5)
    print(f"Test for parent. Insert {5}:", T(b2.array))
    print(b2.parent(2))

    c = list(map(str, range(15, 0, -1)))
    c = zip(c, range(len(c), -1, -1))
    c = PriorQueue(dict(c))
    print("start array:", T(c.array))
    c.build_min_heap()
    print("Test 4.1: Build-Min-Heap", "\tc-heap:\n", T(c.array))
    print("extracted min =", c.heap_extract_min())
    print("array after extracted:", T(c.array))
    c.min_heap_insert("17", 1)
    print("array after insertion:", T(c.array))
    c.build_max_heap()
    print("Max-Heap:", T(c.array))
    c.max_heap_insert("Max-Heap_insert", 700)
    print(f"After insert {700}:", T(c.array))