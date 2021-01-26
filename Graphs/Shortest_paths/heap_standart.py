def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)


def build_min_heap(array):
    for i in reversed(range(len(array) // 2)):
        min_heapify(array, i)

if __name__ == "__main__":
    A = [10, 50, 3, 8, 2]
    a2 = [500, 400, 200, 100, 150, 1, 10]
    build_min_heap(A)
    build_min_heap(a2)
    print(A)
    print(a2)