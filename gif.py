import numpy as np
import sorting.sort as sort
import sorting.animation as animate


def remove_copies(data: list) -> list:
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
                     title: str='Sort', path: str=''):
    sorting_data.clear()
    sorting_algorithm(array)
    sorting_data = remove_copies(sorting_data)
    animate.arrays_2_gif(sorting_data, title=title, path=path, frame_path='tmp/')


d1 = list(np.random.randint(0, 50, 100))
d2 = d1.copy()
d3 = d1.copy()
d4 = d1.copy()


# Merge Sort
make_sorting_gif(d1, sort.MERGE_DATA,
                 sorting_algorithm=sort.merge_sort, title='Merge Sort',
                 path='gif/merge_sort')

# Count Sort
make_sorting_gif(d2, sort.COUNT_DATA,
                 sorting_algorithm=sort.count_sort, title='Count Sort',
                 path='gif/count_sort')

# Comb Sort
make_sorting_gif(d3, sort.COMB_DATA,
                 sorting_algorithm=sort.comb_sort, title='Comb Sort',
                 path='gif/comb_sort')

# Shell Sort
make_sorting_gif(d4, sort.SHELL_DATA,
                 sorting_algorithm=sort.shell_sort, title='Shell Sort',
                 path='gif/shell_sort')
