class Heap(object):
    """ 
    For [*dict.items()] style -> list of tuples of pair values: (name_vertex, distance_to_vertex).
    distance_to_vertex : sum of weights of edges from source vertex to the vertex.
    
    self.d : dict with actual distance's values.
    self.array : array of pointers to self.d with some heap-order.
    """

    def __init__(self, distances: dict, key=None):
        self.d = distances
        if isinstance(distances, dict):
            self.array = [*distances]
        self._hs = None
        if key == "min":
            self.build_min_heap()
        if key == "max":
            self.build_max_heap()

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @property
    def heap_size(self):
        if self._hs == None:
            self.heap_size = len(self.array)
        return self._hs

    @heap_size.setter
    def heap_size(self, i):
        self._hs = i

    def max_heapify(self, i):
        """ self.array[i] - it is key of vertex. """
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.d[self.array[l]] > self.d[self.array[i]]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.d[self.array[r]] > self.d[self.array[largest]]:
            largest = r
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.max_heapify(largest)

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.d[self.array[l]] < self.d[self.array[i]]:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.d[self.array[r]] < self.d[self.array[smallest]]:
            smallest = r
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.min_heapify(smallest)

    def build_max_heap(self):
        for i in range(len(self.array) // 2 - 1, -1, -1):  # range(len(self.array)//2 - 1, -1, -1):
            self.max_heapify(i)

    def build_min_heap(self):
        for i in range(len(self.array) // 2 - 1, -1, -1):  # reversed(range(len(self.array)//2)):
            self.min_heapify(i)


class PriorQueue(Heap):

    def heap_extract_max(self):
        if self.heap_size < 1:
            raise IndexError("The queue is empty.")
        max = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.array.pop()
        self.heap_size -= 1
        self.max_heapify(0)
        return max

    def heap_extract_min(self):
        if self.heap_size < 1:
            raise IndexError("The queue is empty.")
        min = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.array.pop()
        self.heap_size -= 1
        self.min_heapify(0)
        return min

    def heap_increase_key(self, i, key):
        if key < self.d[self.array[i]]:
            raise ValueError("new key is smaller than current key")
        self.d[self.array[i]] = key
        while i > 0 and self.d[self.array[Heap.parent(i)]] < self.d[self.array[i]]:
            self.array[i], self.array[Heap.parent(i)] = self.array[Heap.parent(i)], self.array[i]
            i = Heap.parent(i)

    def heap_decrease_key(self, i, key):
        if key > self.d[self.array[i]]:
            return None  # raise ValueError("new key is bigger than current key")
        self.d[self.array[i]] = key
        while i > 0 and self.d[self.array[Heap.parent(i)]] > self.d[self.array[i]]:
            self.array[i], self.array[Heap.parent(i)] = self.array[Heap.parent(i)], self.array[i]
            i = Heap.parent(i)

    def max_heap_insert(self, key, val):
        """
        The part not use in Dijkstra now and not done.
        In previous version it was like 'min_heap_insert' method and worked.
        Now it's work, but not integrated in Dijkstra.
        """
        self.heap_size += 1
        self.array.append(key)
        self.d[key] = float('-inf')
        self.heap_increase_key(self.heap_size - 1, val)


    def min_heap_insert(self, key, val):
        self.heap_size += 1
        self.array.append(key)
        self.d[key] = float('inf')
        self.heap_decrease_key(self.heap_size - 1, val)


if __name__ == "__main__":
    A = dict(zip(["a", "b", "c", "d", "e"], [10, 50, 3, 8, 2]))
    A = Heap(A, "max")
    print("Test 1.1: Build-Max-Heap", A.array)
    print("Test 1.1: Build-Max-Heap", [A.d[key] for key in A.array])
    A = Heap(A.d, "min")
    print("Test 1.2: Build-Min-Heap", A.array)
    print("Test 1.2: Build-Min-Heap", [A.d[key] for key in A.array])
    #
    a2 = dict(zip(["A", "B", "C", "D", "E", "F", "G"], [500, 400, 200, 100, 150, 1, 10]))
    a2 = Heap(a2, "max")
    # a2.build_max_heap()
    print("Test 2.1: Build-Max-Heap", a2.array)
    print("Test 2.1: Build-Max-Heap", [a2.d[key] for key in a2.array])
    a2.build_min_heap()
    print("Test 2.2: Build-Min-Heap", a2.array)
    print("Test 2.2: Build-Min-Heap", [a2.d[key] for key in a2.array])

    B = zip(["a", "b", "c", "d", "e"], [10, 50, 3, 8, 2])
    B = PriorQueue(dict(B))
    B.build_min_heap()
    print("Test 3.1: Build-Min-Heap", "\tB-heap:\n", B.array)
    print("Test 3.1: Build-Min-Heap", [B.d[key] for key in B.array])
    print("extracted min =", B.heap_extract_min())
    label = "array after extracted:"
    print(label, B.array, "\n",
          label, [B.d[key] for key in B.array])
    # B.min_heap_insert("min_insert", 1)
    # label = "after insertion 1 to heap B:"
    # print(label, B.array, "\n",
    #       label, [B.d[key] for key in B.array])
    # B.min_heap_insert("min_insert", 4)
    # print("after insertion 4 to heap B:", B.array)
    # print("after insertion 4 to heap B:", [B.d[key] for key in B.array])

    b2 = zip(["A", "B", "C", "D", "E", "F", "G"], [500, 400, 200, 100, 150, 1, 10])
    b2 = PriorQueue(dict(b2))
    b2.build_min_heap()
    print("Test 4.1: Build-Min-Heap", "\tb2-heap:\n", b2.array)
    print("Test 4.1: Build-Min-Heap", "\tb2-heap:\n", [b2.d[key] for key in b2.array])
    print("extracted min =", b2.heap_extract_min())
    print("array after extracted:", b2.array)
    print("array after extracted:", [b2.d[key] for key in b2.array])
    # b2.min_heap_insert("max_insert", 600)
    # print("after insertion 600 to heap b2:", b2.array)
    # print("after insertion 600 to heap b2:", [b2.d[key] for key in b2.array])
    b2.build_max_heap()
    print("Max-Heap:", b2.array)
    print("Max-Heap:", [b2.d[key] for key in b2.array])
    b2.max_heap_insert("Max-Heap_insert", 700) #  ("Max-Heap_insert", 700)
    print(f"After insert {700}:", b2.array)
    print(f"After insert {700}:", [b2.d[key] for key in b2.array])
    # b2.build_min_heap()
    # print("Min-Heap:", b2.array)
    # print("Min-Heap:", [b2.d[key] for key in b2.array])
    # b2.min_heap_insert("min_insert", 0.5)
    # print(f"After insert {0.5}:", b2.array)
    # print(f"After insert {0.5}:", [b2.d[key] for key in b2.array])
    # b2.min_heap_insert("round", 5)
    # print(f"Test for parent. Insert {5}:", b2.array)
    # print(f"Test for parent. Insert {5}:", [b2.d[key] for key in b2.array])
    # print(b2.parent(2))
    #
    c = list(map(str, range(15, 0, -1)))
    c = zip(c, range(len(c), -1, -1))
    c = PriorQueue(dict(c))
    print("start array:", c.array)
    print("start array:", [c.d[key] for key in c.array])
    c.build_min_heap()
    print("Test 4.1: Build-Min-Heap", "\tc-heap:\n", c.array)
    print("Test 4.1: Build-Min-Heap", "\tc-heap:\n", [c.d[key] for key in c.array])
    print("extracted min =", c.heap_extract_min())
    print("array after extracted:", c.array)
    print("array after extracted:", [c.d[key] for key in c.array])
    # c.min_heap_insert("17", 1)
    # print("array after insertion:", c.array)
    # print("array after insertion:", [c.d[key] for key in c.array])
    c.build_max_heap()
    print("Max-Heap:", c.array)
    print("Max-Heap:", [c.d[key] for key in c.array])
    c.max_heap_insert("Max-Heap_insert", 700)
    print(f"After insert {700}:", c.array)
    print(f"After insert {700}:", [c.d[key] for key in c.array])
    test = PriorQueue({"a": 1, "b": 2}, "min")
    test.d["a"] = 5
    test.build_min_heap()