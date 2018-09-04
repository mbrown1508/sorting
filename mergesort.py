from constants import *
from math import sqrt, ceil


def merge_sort(array):
    array_length = len(array)
    jump = 1
    for i in range(1, determine_levels(len(array)) + 1):
        loops = array_length//(jump*2)
        for loop in range(loops):
            array1 = array[loop*(jump*2):loop*(jump*2)+jump]
            array2 = array[loop * (jump * 2) + jump:(loop+1) * (jump * 2)]
            merge_arrays(array, array1, array2, loop, jump, jump)

        # Deal with the odd amount remaining
        remaining = array_length % (jump * 2)
        if remaining > jump:
            array1 = array[loops*(jump*2):loops*(jump*2)+jump]
            array2 = array[loops * (jump * 2) + jump:]
            merge_arrays(array, array1, array2, loops, jump, len(array2))

        jump = jump * 2
    return array


def merge_arrays(array, array1, array2, loop, jump, array2index_target):
    array1index = 0
    array2index = 0
    for index in range(loop * (jump * 2), (loop + 1) * (jump * 2)):
        if array1[array1index] < array2[array2index]:
            array[index] = array1[array1index]
            array1index += 1
            if array1index == jump:
                for remaining in array2[array2index:]:
                    index += 1
                    array[index] = remaining
                break
        else:
            array[index] = array2[array2index]
            array2index += 1
            if array2index == array2index_target:
                for remaining in array1[array1index:]:
                    index += 1
                    array[index] = remaining
                break


def determine_levels(array_length):
    levels = 0
    while True:
        array_length = int(array_length/2)
        levels += 1
        if array_length == 0:
            break
    return levels


def merge_sort_generator(array):
    from_array = array[:]
    to_array = array[:]
    length = len(array)
    jump = 1

    for i in range(1, determine_levels(len(array))+1):
        current_index = 0

        index1 = -int(jump)
        index2 = 0

        for x in range(int(ceil(length/(jump*2)))):
            target_array = []
            compare_array = []
            start_index = current_index

            index1 += int(jump)
            index2 += int(jump)

            max_index1 = index1 + int(jump)
            max_index2 = index2 + int(jump)

            if max_index2 > length:
                if max_index1 >= length:
                    loops = length - index1
                    max_index1 = length
                    max_index2 = length
                else:
                    loops = jump+(length-index2)
                    max_index2 = length
            else:
                loops = jump*2

            for _ in range(loops):
                if index1 >= max_index1:
                    target_array.append(index2)
                    index2 += 1
                    current_index += 1
                elif index2 >= max_index2:
                    target_array.append(index1)
                    index1 += 1
                    current_index += 1
                elif from_array[index1] < from_array[index2]:
                    compare_array.append((index1,index2))
                    target_array.append(index1)
                    index1 += 1
                    current_index += 1
                else:
                    compare_array.append((index1, index2))
                    target_array.append(index2)
                    index2 += 1
                    current_index += 1

            for i in range(len(target_array)):
                if len(compare_array) > i:
                    yield COMPARE, to_array, compare_array[i][0], compare_array[i][1]
                j = target_array[i]
                to_array[i+start_index], to_array[j] = to_array[j], to_array[i+start_index]
                target_array = [j if x == (i+start_index) else x for x in target_array]
                yield MOVE, to_array, (i+start_index), j

        from_array, to_array = to_array[:], to_array[:]
        jump = jump * 2
    yield COMPLETE, from_array, -1, -1
