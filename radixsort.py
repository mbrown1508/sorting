from constants import *


def radix_sort(array):
    iterations = len(str(max(array)))
    for i in range(iterations):
        buckets = [[] for x in range(10)]
        for x in array:
            bucket = x // (10**i) % 10
            buckets[bucket].append(x)
        array = [item for sublist in buckets for item in sublist]
    return array


def radix_sort_count(array):
    compare = 0
    swap = 0
    iterations = len(str(max(array)))
    for i in range(iterations):
        buckets = [[] for x in range(10)]
        for x in array:
            bucket = x // (10**i) % 10
            compare += 1
            buckets[bucket].append(x)
            swap += 1
        array = [item for sublist in buckets for item in sublist]
    return array, compare, swap


def radix_sort_generator(array):
    iterations = len(str(max(array)))
    for i in range(iterations):
        buckets = [[] for x in range(10)]
        for x in range(len(array)):
            bucket = array[x] // (10**i) % 10
            yield COMPARE, array, x, x
            buckets[bucket].append(x)

        target_array = [item for sublist in buckets for item in sublist]
        for i in range(len(target_array)):
            j = target_array[i]
            array[i], array[j] = array[j], array[i]
            target_array = [j if x==i else x for x in target_array]
            yield MOVE, array, i, j

    yield COMPLETE, array, -1, -1


