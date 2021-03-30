from hashfunc_2sum_v01 import Hashtable

def two_sum(group, hashtable):
    """
    Summator for 2-SUM algorithm via hash table.
    """
    c = 10000
    sums = {}

    # nearest
    for i in hashtable[group]:
        if len(hashtable[group]) > 1:
            for j in hashtable[group]:
                if -c <= i + j <= c:
                    sums[i + j] = True

    if group - c in hashtable:
        for i in hashtable[group]:
            for j in hashtable[group - c]:
                if -c <= i + j <= c:
                    sums[i + j] = True

    if group + c in hashtable:
        for i in hashtable[group]:
            for j in hashtable[group + c]:
                if -c <= i + j <= c:
                    sums[i + j] = True

    return sums



    for group in [*hashtable]:
        # if isinstance(hashtable[group], int):
        #     hashtable[group] = [hashtable[group]]
        elems = [i for i in hashtable[group]]
        if not len(elems) == 1:
            for i in elems:
                for j in elems:
                    sums[i + j] = True

        if group - c in hashtable:
            nearest = [i for i in hashtable[group - c]]
            for i in elems:
                for j in nearest:
                    if -c/2 <= i + j <= c/2:
                        sums[i + j] = True

        if group + c in hashtable:
            nearest = [i for i in hashtable[group + c]]
            for i in elems:
                for j in nearest:
                    if -c/2 <= i + j <= c/2:
                        sums[i + j] = True

        return sums



if __name__ == "__main__":
    file = open("../task3_2sum.txt", "r")
    data = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
    data = list(map(int, data[:-1]))
    hashtable = Hashtable(data)
    result = {}
    for key in data:
    for group in [*hashtable.hashtable]:
        result.update(two_sum(group, hashtable.hashtable))
    # result = summator(hashtable.hashtable)
    print(len(result))
    #
    # lst = []
    # count = 0
    # for t in range(-10000, 10001):
    #     marker = TwoSum_HashTable(data, hashtable, t)
    #     if marker:
    #         count += 1
    #         lst.append(marker)
    #         print(marker, f"x + y = {sum(marker)}")
    #
    #     # if count % 50 == 0:
    #     #     print("count =", count)
    # print('Via hash table: ' + str(count))
