def twosum_hashtable(t, x):
    global count
    global lst
    global hashtable
    y = t - x
    if y in hashtable and x != y:
        count += 1
        lst.append((x, y))
        return x, y


if __name__ == "__main__":
    file = open("task3_2sum.txt", "r")
    array = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
    array = list(map(int, array[:-1]))
    hashtable = {x: x for x in array}

    lst = []
    count = 0
    for t in range(-10000, 10001):
        for x in array:
            mark = twosum_hashtable(t, x)
            if mark:
                print(mark, sum(mark), f"count = {count}")

        # progress-bar
        stage = t % int(1 / 10 * 10**4)
        print(f"stage : {stage}")
        # if stage == 0:
        #     print(f"count = {count}")


                # print(lst[stage - 5: stage + 1])
