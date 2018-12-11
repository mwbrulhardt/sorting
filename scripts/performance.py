import sorting.sort as sort
import pandas as pd
import numpy as np

N = 1000

data = {}
data['low'] = []
data['high'] = []
data['range'] = []
data['size'] = []
data['merge_time'] = []
data['count_time'] = []
data['comb_time'] = []
data['shell_time'] = []
data['heap_time'] = []
data['binary_insertion_time'] = []

for _ in range(N):
    array_range = np.random.randint(0, 10000, 2)

    low = min(array_range)
    data['low'].append(low)

    high = max(array_range)
    data['high'].append(high)

    data['range'].append(high - low)

    n = np.random.randint(10, 5000)
    data['size'].append(n)

    # Generate an array to be sorted
    a1 = np.random.randint(low=low, high=high, size=n)
    a2 = a1.copy()
    a3 = a1.copy()
    a4 = a1.copy()
    a5 = a1.copy()
    a6 = list(a1.copy())

    # Calculate times for each sorting algorithm
    merge_time = sort.performance(algorithm=sort.merge_sort, data=a1)
    count_time = sort.performance(algorithm=sort.count_sort, data=a2)
    comb_time = sort.performance(algorithm=sort.comb_sort, data=a3)
    shell_time = sort.performance(algorithm=sort.shell_sort, data=a4)
    heap_time = sort.performance(algorithm=sort.heap_sort, data=a5)
    binary_insertion_time = sort.performance(algorithm=sort.binary_insertion_sort, data=a6)

    # Add collected time to the 'data' dictionary
    data['merge_time'].append(merge_time)
    data['count_time'].append(count_time)
    data['comb_time'].append(comb_time)
    data['shell_time'].append(shell_time)
    data['heap_time'].append(heap_time)
    data['binary_insertion_time'].append(binary_insertion_time)

df = pd.DataFrame.from_dict(data)
result = df.sort_values(['size', 'range'], ascending=[1, 1])
result.to_csv('../data/sorting_data.csv', index=False)