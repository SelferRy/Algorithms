def TwoSum_HashTable(lst, hashTable, target):
    '''
    2-SUM algorithm via hash table.

    O(n) time.
    '''

    # hashTable = dict()

    # for x in lst:
    #     hashTable[x] = True

    for x in lst:
        y = target - x
        if y in hashTable and x != y:
            return (x, y)


if __name__ == "__main__":
    file = open("task3_2sum.txt", "r")
    data = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
    data = list(map(int, data[:-1]))
    hashtable = {x: True for x in data}

    count = 0
    for t in range(-10000, 10001):
        if TwoSum_HashTable(data, hashtable, t):
            count += 1
        if count % 50 == 0:
            print("count =", count)
    print('Via hash table: ' + str(count))
