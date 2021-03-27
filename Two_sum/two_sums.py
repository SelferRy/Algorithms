file = open("task3_2sum.txt", "r")
array = file.read().split("\n")  # # file.readlines() # [line.split("\n") for line in file.readlines()]
array = list(map(int, array[:-1]))

hashtable = {x: x for x in array}
lst = []
count = 0
for x in array:
    for t in range(-10000, 10001):
        y = t - x
        if y in hashtable and x != y:
            count += 1
        if count % 50 == 0:
            print(count, x, y, x + y, sep="\n", end="\n" * 2)
