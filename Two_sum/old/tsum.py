# 'straightforward'-version of 2-sum

def TwoSum_HashTable(lst, hashTable, target):
    """
    2-SUM algorithm via hash table.

    O(n) time.
    """
    for x in lst:
        y = target - x
        if y in hashTable and x != y:
            return x, y


if __name__ == "__main__":
    file = open("../data_2sum.txt", "r")
    data = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
    data = list(map(int, data[:-1]))
    hashtable = {x: True for x in data}

    lst = []
    count = 0
    for t in range(-10000, 10001):
        marker = TwoSum_HashTable(data, hashtable, t)
        if marker:
            count += 1
            lst.append(marker)
            print(marker, f"x + y = {sum(marker)}")

        # if count % 50 == 0:
        #     print("count =", count)
    print('Via hash table: ' + str(count))
