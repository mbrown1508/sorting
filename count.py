from tabulate import tabulate
from bubblesort import bubble_sort_count
from itersort import iter_sort_count
from radixsort import radix_sort_count
from constants import *


def verify(array):
    for a, b in zip(array, already_sorted):
        if a != b:
            raise(Exception('Not Sorted - {}'.format(array)))


variations = [iter_sort_count, bubble_sort_count, radix_sort_count]
str_variations = ['iter_sort', 'bubble_sort', 'radix_sort_count']

table = []
for i, (name, variation) in enumerate(zip(str_variations, variations)):
    table.append([name])

    array, compares, swaps = variation(already_sorted[:])
    table[i].append((compares,swaps))
    verify(array)

    array, compares, swaps = variation(reverse[:])
    table[i].append((compares, swaps))
    verify(array)

    for shuffled_array in shuffle_arrays:
        array, compares, swaps = variation(shuffled_array[:])
        table[i].append((compares, swaps))
        verify(array)

print(tabulate(table, headers=['Algorithim', 'already_storted', 'reversed']+['shuffled {}'.format(x) for x in range(5)]))
