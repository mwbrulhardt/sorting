# Sorting Algorithm Analysis

In this project, we have implemented several sorting algorithms and have done some analysis on each one of them. The implemented algorithms are as follows:
* **Merge Sort**
* **Count Sort**
* **Comb Sort**
* **Shell Sort**
* **Heap Sort**
* **Binary Insertion Sort**

Then for each of these algorithms you can analyze how long it takes to sort a given list, you may also create a gif out of the data you are trying to sort by using the gif.py module.

## Getting Started

In order to use this project you can just clone this project onto your computer as follows:
```
git clone https://github.com/mwbrulhardt/sorting.git
```

## Examples 
In order to sort an array, the following code may be used as an example of how to do this. In this case, merge sort is chosen as the method for sorting.
```
import sorting.sort as sort
data = [5, 2, 3, 6, 4, 7, 98]
sort.merge_sort(data)
```
In order to time an algorithm on a given array the following code should be used.
```
import sorting.sort as sort
data = [5, 2, 3, 6, 4, 7, 98]
t = sort.performance(algorithm=sort.merge_sort, data=data)
```
The value of t will be the time it took for the algorithm to sort the given data, and this time will be in milliseconds.

In addition, if one would like to make a gif with a particular sorting algorithm, the following code can be used as a way to do that. The merge sort algorithm will be used again in this example.

```
import sorting.sort as sort
from sorting.gif import make_sorting_gif

data = [5, 2, 3, 6, 4, 7, 98]
make_sorting_gif(d1, sorting_data=sort.MERGE_DATA,
                 sorting_algorithm=sort.merge_sort, title='Merge Sort',
                 path='gif/merge_sort')
```
The parameter sorting_data is of type is a list of arrays. It is the list of arrays that gets created while sorting the algorithm. It takes a snapshot of the array being sorted at each time step and creates a list of them, to be then used to make each image for the gif.

## Prerequisites

Some things you will need in order to use the software are:
* pandas
* matplotlib
* numpy
* imageio

## Authors

* **Matthew Brulhardt**
* **Morgan Mars**
* **Andreas Lietzau**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
