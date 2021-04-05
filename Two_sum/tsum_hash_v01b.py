# 'inplace'-version of 2-sum

from hashtable import Hashtable
import time

def two_sum(data, hashtable, c=10000):
    """
    Summator for 2-SUM algorithm via hash table.
    """
    global sums
    for value in data:
        group = Hashtable.group(value)

        # ===== nearest pairs =====
        for key in [group, group - c, group + c, -group, -group - c, -group + c]:
            if key in hashtable:
                for i in hashtable[key]:
                    if -c <= value + i <= c:
                        sums[value + i] = True


if __name__ == "__main__":
    start_time = time.time()
    file = open("../data_2sum.txt", "r")
    data = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
    data = list(map(int, data[:-1]))
    hashtable = Hashtable(data)
    sums = {}
    two_sum(data, hashtable.hashtable)
    print(len(sums))
    print("--- %s seconds ---" % (time.time() - start_time))