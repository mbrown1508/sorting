from constants import *
from math import inf

# Speed optimised
def selection_sort(array):
    for i in range(len(array)-1):
        lowest = inf
        index = -1
        for j in range(i, len(array)):
            if array[j] < lowest:
                index = j
                lowest = array[j]
        array[i], array[index] = array[index], array[i]
    return array


# Counter
def selection_sort_count(array):
    compare = 0
    swap = 0
    for i in range(len(array)-1):
        lowest = inf
        index = -1
        for j in range(i, len(array)):
            compare += 1
            if array[j] < lowest:
                index = j
                lowest = array[j]
        array[i], array[index] = array[index], array[i]
        swap += 1
    return array, compare, swap


# Generator
def selection_sort_generator(array):
    for i in range(len(array)-1):
        lowest = inf
        index = -1
        for j in range(i, len(array)):
            yield COMPARE, array, j, j
            if array[j] < lowest:
                index = j
                lowest = array[j]
        array[i], array[index] = array[index], array[i]
        yield MOVE, array, i, index
    yield COMPLETE, array, -1, -1

