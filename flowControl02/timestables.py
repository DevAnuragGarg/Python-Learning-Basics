# sequence can be string or range, but python has other sequences that we can iterate over
for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(i, j, i * j))
