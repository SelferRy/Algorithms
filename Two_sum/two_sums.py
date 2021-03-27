def twosum_hashtable(t):
    global array
    global hashtable
    for x in array:
        y = t - x
        if y in hashtable and x != y:
            return x, y


if __name__ == "__main__":
    file = open("task3_2sum.txt", "r")
    array = file.read().split("\n")
    array = list(map(int, array[:-1]))
    hashtable = {x: True for x in array}

    lst = []
    count = 0
    for t in range(-10000, 10001):
        mark = twosum_hashtable(t)
        if mark:
            count += 1
            lst.append(mark)
            print(mark, sum(mark), f"count = {count}")

        # progress-bar
        if t % 100 == 0:
            print("="*8 + "\nProgress-bar:\t",
                  f"{(t/(10**4) + 1)/2},", f"count = {count}",
                  end="\n" + "="*8 + "\n")
