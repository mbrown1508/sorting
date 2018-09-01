from random import randint
from timeit import timeit

iterations = 100
length = 1000

COMPARE = 0
MOVE = 1
COMPLETE = 2

unsorted_array_short = [3,4,8,1,9,6,5,0]
unsorted_array_long = [randint(0,length) for _ in range(length)]


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def iter_sort(array):
    for i in range(len(array)-1):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array


def almost_bubble_sort(array):
    for i in range(len(array)-1):
        swapped = False
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                swapped = True
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
        if not swapped:
            return array
    return array


def lachlan_bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array


def bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        swapped = False
        for j in range(i):
            if array[j] > array[j+1]:
                swapped = True
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
        if not swapped:
            return array
    return array


sorted_array = bubble_sort(unsorted_array_short)
print(sorted_array)


# Bubble sort
sorted_array = iter_sort(unsorted_array_short)
#print(sorted_array)

wrapped = wrapper(iter_sort, unsorted_array_long)
result = timeit(wrapped, number=iterations)
print('Iter sort list_length={} in {:.4f}ms'.format(length, result/iterations*1000))


# Bubble sort
sorted_array = almost_bubble_sort(unsorted_array_short)
#print(sorted_array)

wrapped = wrapper(almost_bubble_sort, unsorted_array_long)
result = timeit(wrapped, number=iterations)
print('Almost Bubblesort list_length={} in {:.4f}ms'.format(length, result/iterations*1000))


# Bubble sort
sorted_array = lachlan_bubble_sort(unsorted_array_short)
#print(sorted_array)

wrapped = wrapper(lachlan_bubble_sort, unsorted_array_long)
result = timeit(wrapped, number=iterations)
print('Lachlan Bubblesort list_length={} in {:.4f}ms'.format(length, result/iterations*1000))


# Bubble sort
sorted_array = bubble_sort(unsorted_array_short)
#print(sorted_array)

wrapped = wrapper(bubble_sort, unsorted_array_long)
result = timeit(wrapped, number=iterations)
print('Bubblesort list_length={} in {:.4f}ms'.format(length, result/iterations*1000))

# Builtin
sorted_array = sorted(unsorted_array_short)
#print(sorted_array)

wrapped = wrapper(sorted, unsorted_array_long)
result = timeit(wrapped, number=iterations)
print('Builtin list_length={} in {:.4f}ms'.format(length, result/iterations*1000))