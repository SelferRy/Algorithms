# import numpy as np

class Heap(object):

    def __init__(self, array):
        self.array = array

    def Parent(self, i):
        return i // 2

    def Left(self, i):
        return 2 * i

    def Right(self, i):
        return 2*i + 1

    @property
    def heap_size(self):
        return len(self.array)

    def Min_heapify(self, A, i):
        A = Heap(A) # self.array # self.Instance.heap_size(A)
        l = self.Left(i)
        r = self.Right(i)
        if l <= A.heap_size and A[l] < A[i]:
            smaller = l
        else:
            smaller = i
        if r <= A.heap_size and A[r] < A[smaller]:
            smaller = r
        if smaller != i:
            A[i], A[smaller] = A[smaller], A[i]
            self.Min_heapify(A, smaller)


if __name__ == "__main__":
    A = [10, 5, 3, 8, 2]
    Heap(A).Min_heapify(A, 1)
    print(A)