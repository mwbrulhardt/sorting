import numpy as np
import sorting.sort as sort
import sorting.animation as animate

from functools import partial


def remove_copies(data: list) -> list:
    """Creates a unique list of arrays given a list of arrays containing
    identical arrays.

    Param:
        data (list[list[float or int]]): a list of lists of comparable items

    Return
        arrays: the unique list with no repeated arrays
    """
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


def make_sorting_gif(array: list, sorting_data: list, sorting_algorithm: callable=None,
                     title: str='Sort', path: str='') -> None:
    """Creates a gif from an array and a sorting algorithm.

    Given an array, a list of lists for the sorting algorithms, a sorting
    algorithm, a title for the gif, and a path to save the gif, the function
    then creates a gif for the particular sorting algorithm on the specified
    array and saves it to the specified path.

    Params:
        array (list[list[float or int]]): a list of comparable items
        sorting_data (list[list[float or int]]):
        sorting_algorithm (callable): the sorting algorithm to be used
        title: the title of the gif
        path: the path to save the gif to
    """
    sorting_data.clear()
    sorting_algorithm = partial(sorting_algorithm, log=True)
    sorting_algorithm(array)
    sorting_data = remove_copies(sorting_data)
    animate.arrays_2_gif(sorting_data, title=title, path=path, frame_path='tmp/')


d1 = list(np.random.randint(0, 50, 100))
d2 = d1.copy()
d3 = d1.copy()
d4 = d1.copy()

# Create gifs for the specified four algorithms.

# Merge Sort
make_sorting_gif(d1, sorting_data=sort.MERGE_DATA,
                 sorting_algorithm=sort.merge_sort, title='Merge Sort',
                 path='gif/merge_sort')

# Count Sort
make_sorting_gif(d2, sorting_data=sort.COUNT_DATA,
                 sorting_algorithm=sort.count_sort, title='Count Sort',
                 path='gif/count_sort')

# Comb Sort
make_sorting_gif(d3, sorting_data=sort.COMB_DATA,
                 sorting_algorithm=sort.comb_sort, title='Comb Sort',
                 path='gif/comb_sort')

# Shell Sort
make_sorting_gif(d4, sorting_data=sort.SHELL_DATA,
                 sorting_algorithm=sort.shell_sort, title='Shell Sort',
                 path='gif/shell_sort')
