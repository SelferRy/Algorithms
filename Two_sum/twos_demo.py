def TwoSum_HashTable(lst, target):
    '''
    2-SUM algorithm via hash table.

    O(n) time.
    '''

    hashTable = dict()

    for x in lst:
        hashTable[x] = True

    for x in lst:
        y = target - x
        if y in hashTable and x != y:
            return (x, y)

    return None


def main():
    file = open("task3_2sum.txt", "r")
    data = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
    data = list(map(int, data[:-1]))

    count = 0
    for i, t in enumerate(range(-10000, 10001)):
        if i % 2000:
            print("Still work")
        if TwoSum_HashTable(data, t):
            count += 1
    print('Via hash table: ' + str(count))

if __name__ == "__main__":
    main()