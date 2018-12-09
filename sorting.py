

import time
MERGE_DATA = []
COUNT_DATA = []
COMB_DATA = []
SHELL_DATA = []
HEAP_DATA = []
BINARY_INSERTION_DATA = []


def performance(algorithm=None, data=None):
    start = time.time()
    algorithm(data)
    end = time.time()
    return (end - start)*1000


# Matt's Code
def _merge(data, first, n1, n2):
    MERGE_DATA.append(data.copy())
    temp = []
    i = i1 = i2 = 0
    while i1 < n1 and i2 < n2:

        if data[first + i1] < data[first + n1 + i2]:
            temp.append(data[first + i1])
            i += 1
            i1 += 1
        else:
            temp.append(data[first + n1 + i2])
            i += 1
            i2 += 1

    while i1 < n1:
        temp.append(data[first + i1])
        i += 1
        i1 += 1

    for i in range(i):
        data[first + i] = temp[i]
    MERGE_DATA.append(data.copy())


def _merge_sort_helper(data, first, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        MERGE_DATA.append(data.copy())
        _merge_sort_helper(data, first, n1)
        _merge_sort_helper(data, first + n1, n2)

        _merge(data, first, n1, n2)


def merge_sort(data):
    return _merge_sort_helper(data, 0, len(data))


def count_sort(data):
    n = len(data)
    k = max(data) + 1

    # Create count array and output array.
    count = [0]*k
    output = [0]*n

    # Get the frequencies of all number in the data array.
    for i in data:
        count[i] += 1

    # Create the cumulative frequency array.
    for i in range(1, k):
        count[i] += count[i-1]

    # Fill in the output array and decrease the frequency values once done.
    for i in data:
        output[count[i]-1] = i
        count[i] -= 1

    COUNT_DATA.append(data.copy())
    # Copy output array into data array.
    for i in range(n):
        COUNT_DATA.append(data.copy())
        data[i] = output[i]


# Andreas's Code
def comb_sort(data):
    gap = len(data)
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True

        for i in range(0, len(data) - gap):
            if data[i] > data[i + gap]:
                dummy = data[i]
                data[i] = data[i + gap]
                data[i + gap] = dummy
                is_sorted = False


def shell_sort(data):
    ciura_gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]

    for gap in ciura_gaps:
        for i in range(gap, len(data)):
            dummy = data[i]
            while (i >= gap) and (data[i - gap] > dummy):
                data[i] = data[i - gap]
                i -= gap
            data[i] = dummy


# Morgan's Code
def _heapify(subtree, heap_size, root_index):

    largest_value_index = root_index
    left_child_index = 2 * root_index + 1
    right_child_index = 2 * root_index + 2

    if left_child_index < heap_size and subtree[root_index] < subtree[left_child_index]:
        largest_value_index = left_child_index

    if right_child_index < heap_size and subtree[largest_value_index] < subtree[right_child_index]:
        largest_value_index = right_child_index

    if largest_value_index != root_index:
        subtree[root_index], subtree[largest_value_index] = subtree[largest_value_index], subtree[root_index]

        _heapify(subtree, heap_size, largest_value_index)


def _build_max_heap(unsorted_list, list_length):
    for i in range(list_length, -1, -1):
        _heapify(unsorted_list, list_length, i)


def heap_sort(unsorted_list):
    list_length = len(unsorted_list)

    _build_max_heap(unsorted_list, list_length)

    for i in range(list_length - 1, 0, -1):
        unsorted_list[i], unsorted_list[0] = unsorted_list[0], unsorted_list[i]
        _heapify(unsorted_list, i, 0)

    return unsorted_list


def _binary_search(search_list, next_item, left, right):
    if left == right:
        if next_item > search_list[left]:
            return left + 1
        else:
            return left

    if right < left:
        return left

    midpoint = (left + right) // 2

    if search_list[midpoint] < next_item:
        return _binary_search(search_list, next_item, midpoint + 1, right)
    elif search_list[midpoint] > next_item:
        return _binary_search(search_list, next_item, left, midpoint - 1)
    else:
        return midpoint


def binary_insertion_sort(data):
    for i in range(1, len(data)):
        next_item = data[i]
        insert_position = _binary_search(data, next_item, 0, i - 1)
        data = data[:insert_position] + [next_item] + data[insert_position:i] + data[i + 1:]
    return data


def remove_copies(data) -> list:
    arrays = []
    for a in data:
        # Check if a is in arrays
        contained = False
        for array in arrays:
            # Check if 'a' and 'array' are equal
            equal = True
            for i in range(len(array)):
                if a[i] != array[i]:
                    equal = False
                    break

            if equal:
                contained = True
        if not contained:
            arrays.append(a)
    return arrays
