# Import the required libraries
# Import random to make random array
import random as rand
# Import timeit to use timer
from timeit import default_timer as timer

# Global variable to keep track of insertions made
insertions_made = 0
# Global variable to keep track of comparisons made
comparisons = 0


# Function that performs binary search to find the index to insert the next item
# Accepts the list to search, the value of the next item, and a left and right index
def binary_search(search_list, next_item, left, right):
    # Makes global variable comparisons available to the function
    global comparisons
    # If the index of left and right are the same, then the search has converged.  
    if left == right:
        # Increments comparisons
        comparisons += 1
        # If the value of the next item is greater than the value at the converged-on (found) index,
        # then the next item should be inserted to the right of the found index (inserted at left+1).
        if next_item > search_list[left]:
            return left + 1
        # If the value of the next item is not larger than the value at the found index, then it 
        # should be inserted to the left of the found value. The value of "left" is returned because 
        # the rest of the list is appended after this point. Inserting at "left" will shift the 
        # subsequent values to the right.
        else:
            return left
    # If right is less than left, then we know that the value of the next item is definitely less than
    # the value at left, therefore the next item should be inserted to the left.
    if right < left:
        return left
    # If the values have not yet converged or overshot, then we have to keep searching. This finds the
    # midpoint. The double slash means we want to divide as an integer operation.
    midpoint = (left + right) // 2

    # Increments comparisons
    comparisons += 1
    # If the value at the midpoint is less than the value of the next item, then we know that the final
    # index position will be somewhere to the right of the midpoint. So we call binary_search again, but with
    # the left-most index as midpoint+1.
    if search_list[midpoint] < next_item:
        return binary_search(search_list, next_item, midpoint + 1, right)
    # Likewise, if the value of the midpoint is greater than the next item then the final index is somewhere
    # to the left, so we change the rightmost index as midpoint-1.
    elif search_list[midpoint] > next_item:
        return binary_search(search_list, next_item, left, midpoint - 1)
    # Otherwise, the value at midpoint is equal to the value of the next item, which means we have found the
    # right index, and we can insert there.
    else:
        return midpoint

# Function that performs insertion sort 
# Accepts the list to be sorted    
def insertion_sort(sort_list):
    # Make global variable insertions_made available to the function
    global insertions_made
    # For loop that iterates from 1 to the length of sort_list. Iterates from 1 because we can assume that the 
    # first value is already in its own sorted sublist already.
    for i in range(1, len(sort_list)):
        # The next item to be checked is the value of sort_list at index i
        next_item = sort_list[i]
        # Insert position is found by running binary search recursively with the next_item as an argument.
        insert_position = binary_search(sort_list, next_item, 0, i-1)
        # Sort list is re-made by cutting the next_item out and inserting it in the insert position, and then re
        # creating the list around it.
        sort_list = sort_list[:insert_position] + [next_item] + sort_list[insert_position:i] + sort_list[i+1:]
        # Increments insertions_made
        insertions_made += 1
    # Returns the sorted list
    return sort_list

# Main user interface code, to ask how many items should be sorted
list_length = int(input('How many items would you like to sort? \n'))
# Creates an unsorted list with as many unique integer values as the number of items to be sorted
# Basically, if the user enters 100, there will be values from 1-101 just randomly ordered.
unsorted_list = rand.sample(range(0,list_length),list_length)

# Sets the start variable equal to the timer before running the sort
start = timer()
# Runs the insertion sort on the unsorted list and assigns the output to
# sorted_list
sorted_list = insertion_sort(unsorted_list)
# Sets the end variable equal to the timer after running the sort
end = timer()

# Displays the unsorted and sorted lists.
print(f'first unsorted list: {unsorted_list} \n')

print(f'final sorted list: {sorted_list} \n')

#Displyas the efficiency data (elapsed time, swaps made, comparisons made)
print(f'elapsed time: {end-start}s \n')

print(f'swaps made: {insertions_made} \n')

print(f'comparisons made: {comparisons} \n')