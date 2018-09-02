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