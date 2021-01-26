class Heap(object):

    def __init__(self, array):
        self.array = array
        self._hs = None

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    @property
    def heap_size(self):
        if self._hs == None:
            self.heap_size = len(self.array) - 1
        return self._hs

    @heap_size.setter
    def heap_size(self, i):
        self._hs = i
        return self._hs


    def max_heapify(self, i):
        A = Heap(self.array) # self.array # self.Instance.heap_size(A)
        l = self.left(i)
        r = self.right(i)
        if l < A.heap_size and A.array[l] > A.array[i]:
            largest = l
        else:
            largest = i
        if r < A.heap_size and A.array[r] > A.array[largest]:
            largest = r
        if largest != i:
            A.array[i], A.array[largest] = A.array[largest], A.array[i]
            self.max_heapify(largest)

    def min_heapify(self, i):
        A = Heap(self.array) # self.array # self.Instance.heap_size(A)
        l = self.left(i)
        r = self.right(i)
        if l <= A.heap_size and A.array[l] < A.array[i]:
            smallest = l
        else:
            smallest = i
        if r <= A.heap_size and A.array[r] < A.array[smallest]:
            smallest = r
        if smallest != i:
            A.array[i], A.array[smallest] = A.array[smallest], A.array[i]
            self.min_heapify(smallest)

    def build_max_heap(self):
        self.heap_size = len(self.array)
        for i in range(len(self.array)//2, 0, -1):
            self.max_heapify(i)

    def build_min_heap(self):
        for i in reversed(range(len(self.array)//2)):
            self.min_heapify(i)


class Prior_queue(Heap):

    def heap_extract_max(self):
        if self.heap_size < 1:
            raise IndexError("The queue is empty.")
        max = self.array[0]
        self.array[0] = self.array[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(0)
        return max
    
    def heap_extract_min(self):
        if self.heap_size < 1:
            raise IndexError("The queue is empty.")
        min = self.array[0]
        self.array[0] = self.array[self.heap_size]
        self.heap_size -= 1
        self.min_heapify(0)
        return min


if __name__ == "__main__":
    A = Heap([10, 50, 3, 8, 2])
    A.build_max_heap()
    print(A.array)
    A.build_min_heap()
    print(A.array)

    a2 = Heap([500, 400, 200, 100, 150, 1, 10])
    a2.build_max_heap()
    print(a2.array)
    a2.build_min_heap()
    print(a2.array)


