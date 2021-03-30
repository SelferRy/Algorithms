from hashfunc_2sum_v01 import Hashtable

def summator(hashtable):
    """
    Summator for 2-SUM algorithm via hash table.
    """
    c = 20000
    sums = {}
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
    file = open("../data_2sum.txt", "r")
    data = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
    data = list(map(int, data[:-1]))
    hashtable = Hashtable(data)
    hashtable.shrink_ht()
    result = summator(hashtable.hashtable)
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
