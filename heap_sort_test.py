# Import the required libraries
# Import random to make random array
import random as rand
# Import timeit to use timer
from timeit import default_timer as timer

# Global variable to keep track of swaps made
swaps_made = 0;
# Global variable to keep track of comparisons made
comparisons = 0;

# Function that makes a heap out of a given subtree.
# Accepts the subtree, the heap size, the root index, and the full unsorted list
def heapify(subtree, heap_size, root_index):
    # Makes global variables swaps_made and comparisons available to the function
    global swaps_made
    global comparisons

    # Sets the largest value index equal to the root index
    largest_value_index = root_index
    # Sets the left child index equal to 2 * root_index + 1
    left_child_index = 2 * root_index + 1
    # Sets the right child index equal to 2 * root_index + 2
    right_child_index = 2* root_index + 2
    
    # Increments comparisons
    comparisons += 1
    # If the left child index is smaller than the heap size (exists) 
    # and the value of the subtree at the root index is smaller than the 
    # value of the subtree at the left child index, then the largest value 
    # index is set to the left child index
    if left_child_index < heap_size and subtree[root_index] < subtree[left_child_index]:
        largest_value_index = left_child_index
    
    # Increments comparisons
    comparisons += 1
    # Same, but for the right child index
    if right_child_index < heap_size and subtree[largest_value_index] < subtree[right_child_index]:
        largest_value_index = right_child_index

    # If the largest value index is NOT the root index, then a swap must be made to make a heap.
    if largest_value_index != root_index:
        # Increments swaps made
        swaps_made += 1
        # Swaps the value at the root index and the largest value index
        subtree[root_index],subtree[largest_value_index] = subtree[largest_value_index],subtree[root_index]
        # Then heapify the subtree
        heapify(subtree, heap_size, largest_value_index)

# Function that builds a max heap (heapify the entire list)
# Accepts the unsorted list and the length of the list
def build_max_heap(unsorted_list, list_length):
    # Iterates for the entire length of the list.
    for i in range(list_length, -1, -1):
        heapify(unsorted_list, list_length, i)

# Function that performs the heap sort.
# Accepts the unsorted list.   
def heap_sort(unsorted_list):
    # Makes global variable swaps_made available to the function
    global swaps_made
    list_length = len(unsorted_list)
    
    # Build max heap
    build_max_heap(unsorted_list, list_length)

    # Iterate from the back of the list to the front, swapping the largest
    # value to the back and re-heapifying the list after every largest value
    # is swapped.
    # Visually, this should look like the sorted sublist grows from the right 
    # to the left.
    for i in range(list_length - 1, 0, -1):
        # Increment swaps_made
        swaps_made += 1
        # Swap the first value (largest value) to the left of the growing sublist
        unsorted_list[i], unsorted_list[0] = unsorted_list[0], unsorted_list[i]
        # Heapify the list again
        heapify(unsorted_list, i, 0)
    # Returns the unsorted_list    
    return unsorted_list

# Main user interface code, to ask how many items should be sorted
list_length = int(input('How many items would you like to sort? \n'))
# Creates an unsorted list with as many unique integer values as the number of items to be sorted
# Basically, if the user enters 100, there will be values from 1-101 just randomly ordered.
unsorted_list = rand.sample(range(0,list_length),list_length)

# Prints the unsorted list 
print(f'first unsorted list: {unsorted_list} \n')

# Sets the start variable equal to the timer before running the sort
start = timer()
# Runs the heap sort and assigns the output to sorted_list
sorted_list = heap_sort(unsorted_list)
# Sets the end variable equal to the timer after running the sort
end = timer()

# Prints the sorted list
print(f'final sorted list: {sorted_list} \n')

# Prints the elapsed time
print(f'elapsed time: {end-start}s \n')

# Prints the number of swaps made
print(f'swaps made: {swaps_made} \n')

# Prints the number of comparisons made
print(f'comparisons made: {comparisons} \n')

