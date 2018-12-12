

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
def _merge(data: list, first: int, n1: int, n2: int) -> None:
    """Merges two sorted lists into a single sorted list.

    This function does these operations with respect to a single list. It
    assumes that there are two sorted sub-lists within the list 'data' and
    then merges then together to create one sorted sub-list.

    Params:
        data: a list of comparable items
        first: index of where the first list starts
        n1: length of the first list
        n2: length of the second list
    """
    #MERGE_DATA.append(data.copy())
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
    #MERGE_DATA.append(data.copy())


def _merge_sort_helper(data: list, first: int, n: int) -> None:
    """Helper function for merge sort. 
    
    This function sorts the list 'data' from the index 'first' to the index 
    'n'.
    
    Params:
        data: a list of
        first:
        n:
    """
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        #MERGE_DATA.append(data.copy())
        _merge_sort_helper(data, first, n1)
        _merge_sort_helper(data, first + n1, n2)

        _merge(data, first, n1, n2)


def merge_sort(data: list) -> None:
    return _merge_sort_helper(data, 0, len(data))


def count_sort(data: list, log=True) -> None:
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

    #if log:
        #COUNT_DATA.append(data.copy())
    # Copy output array into data array.
    for i in range(n):
        #if log:
            #COUNT_DATA.append(data.copy())
        data[i] = output[i]


# Andreas's Code
def comb_sort(data: list, log=True) -> None:
    gap = len(data)
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        #if log:
            #COMB_DATA.append(data.copy())

        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True

        for i in range(0, len(data) - gap):
            #if log:
                #COMB_DATA.append(data.copy())
            if data[i] > data[i + gap]:
                dummy = data[i]
                data[i] = data[i + gap]
                data[i + gap] = dummy
                is_sorted = False


def shell_sort(data: list, log=True) -> None:
    ciura_gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]

    for gap in ciura_gaps:
        #if log:
            #SHELL_DATA.append(data.copy())
        for i in range(gap, len(data)):
            #if log:
                #SHELL_DATA.append(data.copy())
            dummy = data[i]
            while (i >= gap) and (data[i - gap] > dummy):
                #if log:
                    #SHELL_DATA.append(data.copy())
                data[i] = data[i - gap]
                i -= gap
            data[i] = dummy


# Morgan's Code
def _heapify(subtree: list, heap_size: int, root):

    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and subtree[root] < subtree[left]:
        largest = left

    if right < heap_size and subtree[largest] < subtree[right]:
        largest = right

    if largest != root:
        subtree[root], subtree[largest] = subtree[largest], subtree[root]

        _heapify(subtree, heap_size, largest)


def _build_max_heap(unsorted_list, list_length):
    for i in range(list_length, -1, -1):
        _heapify(unsorted_list, list_length, i)


def heap_sort(unsorted_list):
    list_length = len(unsorted_list)

    _build_max_heap(unsorted_list, list_length)

    for i in range(list_length - 1, 0, -1):
        unsorted_list[i], unsorted_list[0] = unsorted_list[0], unsorted_list[i]
        _heapify(unsorted_list, i, 0)


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


if __name__ == '__main__':

    array = [3,2]

    array = binary_insertion_sort(array)
    print(array)