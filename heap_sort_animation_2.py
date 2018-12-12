# Import the required libraries
# Import matplotlib for plotting
import matplotlib.pyplot as plt
# Import numpy for array functions
import numpy as np
# Import random to make random array
import random as rand
# Import imageio to make the gif
import imageio

# Global variable for tracking swaps
swaps = 0
# Global variable for tracking when a max heap has been made
max_heap_count = 0
# Global variable for holding the read images
images = []
# Global variable for holding the image names 
image_names = []

# Function that makes a heap out of a given subtree.
# Accepts the subtree, the heap size, the root index, and the full unsorted list
def heapify(subtree, heap_size, root_index, unsorted_list):
    # Makes the global variable swaps available to the function
    global swaps
    # Sets the largest value index equal to the root index
    largest_value_index = root_index
    # Sets the left child index equal to 2 * root_index + 1
    left_child_index = 2 * root_index + 1
    # Sets the right child index equal to 2 * root_index + 2
    right_child_index = 2* root_index + 2
    
    # If the left child index is smaller than the heap size (exists) 
    # and the value of the subtree at the root index is smaller than the 
    # value of the subtree at the left child index, then the largest value 
    # index is set to the left child index
    if left_child_index < heap_size and subtree[root_index] < subtree[left_child_index]:
        largest_value_index = left_child_index
    
    # Same, but for the right child index
    if right_child_index < heap_size and subtree[largest_value_index] < subtree[right_child_index]:
        largest_value_index = right_child_index

    # If the largest value index is NOT the root index, then a swap must be made to make a heap.
    if largest_value_index != root_index:
        # Swaps the value at the root index and the largest value index
        subtree[root_index],subtree[largest_value_index] = subtree[largest_value_index],subtree[root_index]
        # Increment swaps
        swaps += 1
        # Save an image, as a swap has been made and we want to show it
        # This is the only function that unsorted list needs to be used for, as we want to
        # render the image when swaps happen. The unsorted list isn't needed to heapify, as
        # it only really compares 3 values
        save_image(unsorted_list, root_index, largest_value_index)
        # Then heapify the subtree, making images of all the swaps as we go
        heapify(subtree, heap_size, largest_value_index, unsorted_list)

# Function that builds a max heap (heapify the entire list)
# Accepts the unsorted list and the length of the list
def build_max_heap(unsorted_list, list_length):
    # Iterates for the entire length of the list.
    for i in range(list_length, -1, -1):
        heapify(unsorted_list, list_length, i, unsorted_list)
    
# Function that performs the heap sort.
# Accepts the unsorted list.
def heap_sort(unsorted_list):
    # Makes global variables swaps and max_heap_count available to the function
    global swaps
    global max_heap_count

    list_length = len(unsorted_list)
    # Build max heap
    build_max_heap(unsorted_list, list_length)

    # Iterate from the back of the list to the front, swapping the largest
    # value to the back and re-heapifying the list after every largest value
    # is swapped.
    # Visually, this should look like the sorted sublist grows from the right 
    # to the left.
    for i in range(list_length - 1, 0, -1):
        # Swap the first value (largest value) to the left of the growing sublist
        unsorted_list[i], unsorted_list[0] = unsorted_list[0], unsorted_list[i]
        # Increment swaps
        swaps += 1
        # Increment max_heap count to color the sorted sublist green
        max_heap_count += 1
        # Save image after the swap
        save_image(unsorted_list, i, 0)
        # Heapify the list again
        heapify(unsorted_list, i, 0, unsorted_list)
    # Returns the unsorted_list
    return unsorted_list

# Function that saves an image to demonstrate how the sorting process works
# Accepts the unsorted list and the indices of the swaps
def save_image(unsorted_list, index_1, index_2):
    # Makes the global variables swaps, images, and max_heap_count
    # available to the function
    global swaps
    global images
    global max_heap_count

    # Clear the plot
    plt.clf()
     # Set the x positions of the bars (use the length of the list as the positions)
    x_pos = np.arange(len(unsorted_list))
    # The heights of the bars correspond to the values of unsorted_list
    height = unsorted_list

    # Variable bars holds the plot
    bars = plt.bar(x_pos, height, width = 0.6)
    # Label the plot
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title("Heap Sort")

    # Color all the bars in the sorted sublist (the number of max heaps 
    # there have been) green
    for j in range(list_length - 1, list_length - 1 - max_heap_count, -1):
        bars[j].set_color('g')
    
    # Set the swapped bars to red. This indicates to the viewer that there 
    # was a swap
    bars[index_1].set_color('r')
    bars[index_2].set_color('r')

    # Save the figure with a file name based on the number of swaps
    plt.savefig(f'heap_sort_images_2/{swaps}.png')
    # Add the newly created filename to the list of image names
    image_names.append(f'heap_sort_images_2/{swaps}.png')

# Main user interface code, to ask how many items should be sorted
list_length = int(input('How many items would you like to sort? \n'))
# Creates an unsorted list with as many unique integer values as the number of items to be sorted
# Basically, if the user enters 100, there will be values from 1-101 just randomly ordered.
unsorted_list = rand.sample(range(1,list_length + 1),list_length)

# Prints the unsorted list 
print(f'first unsorted list: {unsorted_list} \n')

# Runs the heap sort and assigns the output to sorted_list 
sorted_list = heap_sort(unsorted_list)

# Prints the sorted list
print(f'final sorted list: {sorted_list} \n')

# Saves the last image once it has been sorted to be all green
plt.clf()
x_pos = np.arange(len(sorted_list))
height = sorted_list

plt.bar(x_pos, height, width = 0.6, color = 'g')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title("Heap Sort")

plt.savefig(f'heap_sort_images_2/{swaps}.png')
image_names.append(f'heap_sort_images_2/{swaps}.png')

# Code that creates the GIF.
# For loop iterates through the list of images names, reads the data at each file path,
# and appends the data to the images array.
for image_name in image_names:
    images.append(imageio.imread(image_name))
# The imageio uses the images array to feed data into the heap_sort.gif file,
# and loops it only once so that the user can see when the array is finished sorting.
imageio.mimwrite('heap_sort.gif', images, format ='GIF-FI', loop = 1, fps = 10)
