def MergeSort(A, n):
    """
    left/right -- start/end in MergeSort
    """
    temp_arr = [0] * n
    start = 0
    end = n - 1
    return _mergeSort(A, temp_arr, start, end)


def _mergeSort(A, temp_arr, start, end):
    inv_count = 0
    if start < end:
        mid = (start + end) // 2
        inv_count += _mergeSort(A, temp_arr, start, mid)
        inv_count += _mergeSort(A, temp_arr, mid + 1, end)
        inv_count += merge(A, temp_arr, start, mid, end)
    return inv_count


def merge(A, temp_arr, start, mid, end):
    A.append(float("inf"))
    i = start
    j = mid + 1
    inv_count = 0
    for k in range(start, end + 1):
        #         print(A[j], A[i])
        if (i <= mid) & (A[i] <= A[j]):
            temp_arr[k] = A[i]
            i += 1
        elif (j <= end) & (A[i] > A[j]):
            #             print(A[j], A[i])
            temp_arr[k] = A[j]
            j += 1
            inv_count += (mid - i + 1)
        else:
            if i <= mid:
                temp_arr[k] = A[i]
                i += 1
            elif j <= end:
                temp_arr[k] = A[j]
                j += 1
            else:
                raise ValueError("Something wrong...")

    while i <= mid:  # for i in range(i, mid + 1)
        temp_arr[k] = A[i]
        k += 1
        i += 1

    while j <= end:  # for j in range(j, end + 1)
        temp_arr[k] = A[j]
        k += 1
        j += 1

    A[start: end + 1] = temp_arr[start: end + 1]
    A.pop()
    return inv_count


if __name__ == "__main__":
    # Small test-case:
    arr = [1, 20, 6, 4, 5]
    n = len(arr)
    result = MergeSort(arr, n)
    print("Number of inversions are", result)

    # Exam-case:
    file = open("array.txt", "r")
    array = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
    array = list(map(int, array))
    result = MergeSort(array, len(array))
    print(result)
