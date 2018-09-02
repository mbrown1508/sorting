from constants import *
from math import sqrt, ceil

def merge_sort(array):
    from_array = array[:]
    to_array = array[:]
    length = len(array)
    jump = 1

    for i in range(1, int(sqrt(length))+2):
        current_index = 0

        index1 = -int(jump)
        index2 = 0

        for x in range(int(ceil(length/(jump*2)))):
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
                    to_array[current_index] = from_array[index2]
                    index2 += 1
                    current_index += 1
                elif index2 >= max_index2:
                    to_array[current_index] = from_array[index1]
                    index1 += 1
                    current_index += 1
                elif from_array[index1] < from_array[index2]:
                    to_array[current_index] = from_array[index1]
                    index1 += 1
                    current_index += 1
                else:
                    to_array[current_index] = from_array[index2]
                    index2 += 1
                    current_index += 1

        from_array, to_array = to_array, from_array
        jump = jump * 2
    return from_array


def merge_sort_generator(array):
    from_array = array[:]
    to_array = array[:]
    length = len(array)
    jump = 1

    for i in range(1, int(sqrt(length))+2):
        current_index = 0

        index1 = -int(jump)
        index2 = 0

        for x in range(int(ceil(length/(jump*2)))):
            target_array = []
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
                    yield COMPARE, to_array, index1, index2
                    target_array.append(index1)
                    index1 += 1
                    current_index += 1
                else:
                    yield COMPARE, to_array, index1, index2
                    target_array.append(index2)
                    index2 += 1
                    current_index += 1

            for i in range(len(target_array)):

                j = target_array[i]
                to_array[i+start_index], to_array[j] = to_array[j], to_array[i+start_index]
                target_array = [j if x == (i+start_index) else x for x in target_array]
                yield MOVE, to_array, (i+start_index), j

        from_array, to_array = to_array[:], to_array[:]
        jump = jump * 2
    yield COMPLETE, from_array, -1, -1


