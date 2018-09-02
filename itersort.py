from constants import *

# Speed optimised
def iter_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1,i-1,-1):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


# Counter
def iter_sort_count(_array):
    array = _array[:]
    compare = 0
    swap = 0
    for i in range(len(array)-1):
        for j in range(len(array) - 1, i - 1, -1):
            compare += 1
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swap += 1
    return array, compare, swap


# Generator
def iter_sort_generator(array):
    for i in range(len(array)-1):
        for j in range(len(array) - 1, i - 1, -1):
            if array[i] > array[j]:
                yield COMPARE, array, i, j
                array[i], array[j] = array[j], array[i]
                yield MOVE, array, i, j
            else:
                yield COMPARE, array, i, j

    yield COMPLETE, array, -1, -1