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

## Guide for Binary Insertion Sort and Heap Sort
```heap_sort_test.py``` and ```binary_insertion_sort.py```

Both of the programs for these sorting algorithms use the random and timeit libraries so both of these will need to be installed if they are not already prior to running the code.

To use the programs, simply run them. You will be prompted with the question: “How many items would you like to sort?” Enter a number and the program will generate an array of random integers containing the number of elements entered.

The program will output the initial unsorted array, the final sorted array, the elapsed time (how long it took to sort the array), the number of swaps made while sorting, and the number of comparisons made while sorting.

```heap_sort_animation_2.py``` and ```binary_insertion_sort_animation_2.py```

Both of the programs for the animations for these sorting algorithms use the matplotlib, numpy, random, and imageio libraries so these will need to be installed if they are not already prior to running the code.

The binary insertion sort code uploads each frame to a folder called “binary_insertion_sort_images_2” so this folder will need to be created prior to running the program.

The heap sort code uploads each frame to a folder called “heap_sort_images_2” so this folder will need to be created prior to running the program.

Once the above steps are done, simply run the programs. Again, you will be prompted with the question: “How many items would you like to sort?” To get animations that look like the ones submitted, enter 100. 

The GIFS will be saved as “binary_insertion_sort.gif” and heap_sort.gif”

### Prerequisites

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

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
