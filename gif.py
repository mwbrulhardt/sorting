
import numpy as np
import sorting.sorting as srt
import sorting.animation as anim


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


d1 = np.random.randint(0, 50, 100)
d2 = d1.copy()
d3 = d1.copy()
d4 = d1.copy()
d5 = d1.copy()
d6 = d1.copy()


# Make merge sort gif
srt.merge_sort(d1)
MERGE_DATA = remove_copies(srt.MERGE_DATA)
anim.arrays_2_gif(MERGE_DATA, title='Merge Sort', path='gif/merge_sort', frame_path='tmp/')

# Make count sort gif
srt.count_sort(d2)
COUNT_DATA = remove_copies(srt.COUNT_DATA)
anim.arrays_2_gif(COUNT_DATA, title='Count Sort', path='gif/count_sort', frame_path='tmp/')