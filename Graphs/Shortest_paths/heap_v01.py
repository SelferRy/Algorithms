# import numpy as np

class Heap(object):

    # def __init__(self, array):
    #     self.array = array
    #     self._hs = None

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2*i + 1

    # @property
    # def heap_size(self):
    #     if self._hs == None:
    #         self.heap_size = len(self.array)
    #     return self._hs
    #
    # @heap_size.setter
    # def heap_size(self, i):
    #     self._hs = i
    #     return self._hs


    def max_heapify(self, A, i):
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

    def min_heapify(self, A, i):
        A = Heap(self.array) # self.array # self.Instance.heap_size(A)
        l = self.left(i)
        r = self.right(i)
        heap_size = len(self.array) - 1
        if l < heap_size and A.array[l] < A.array[i]:
            smaller = l
        else:
            smaller = i
        if r < heap_size and A.array[r] < A.array[smaller]:
            smaller = r
            A.array[i], A.array[smaller] = A.array[smaller], A.array[i]
            self.min_heapify(smaller)

    def build_max_heap(self):
        self.heap_size = len(self.array)
        for i in range(len(self.array)//2, 0, -1):
            self.max_heapify(i)



if __name__ == "__main__":
    A = Heap([10, 50, 3, 8, 2])
    test = A.build_max_heap()
    print(test)