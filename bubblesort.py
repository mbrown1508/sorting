from constants import *

# Speed Optimised
def bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        swapped = False
        for j in range(i):
            if array[j] > array[j+1]:
                swapped = True
                array[j + 1], array[j] = array[j], array[j + 1]
        if not swapped:
            return array
    return array


# Counter
def bubble_sort_count(_array):
    array = _array[:]
    compare = 0
    swap = 0
    for i in range(len(array)-1,0,-1):
        swapped = False
        for j in range(i):
            compare += 1
            if array[j] > array[j+1]:
                swapped = True
                array[j + 1], array[j] = array[j], array[j + 1]
                swap += 1
        if not swapped:
            return array, compare, swap
    return array, compare, swap


# Generator based
def bubble_sort_generator(array):
    for i in range(len(array) - 1, 0, -1):
        swapped = False
        for j in range(i):
            yield COMPARE, array, j, j + 1
            if array[j] > array[j+1]:
                swapped = True
                array[j + 1], array[j] = array[j], array[j + 1]
                yield MOVE, array, j, j + 1
        if not swapped:
            yield COMPLETE, array, -1, -1
    yield COMPLETE, array, -1, -1