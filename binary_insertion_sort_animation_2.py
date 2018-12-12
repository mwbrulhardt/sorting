# Import the required libraries
# Import matplotlib for plotting
import matplotlib.pyplot as plt
# Import numpy for array functions
import numpy as np
# Import random to make random array
import random as rand
# Import imageio to make the gif
import imageio

# Global variable for tracking insertions 
insertions = 0
# Global variable for tracking number of images
image_counter = 0
# Global variable for holding the read images
images = []
# Global variable for holding the image names 
image_names = []

# Function that performs binary search to find the index to insert the next item
# Accepts the list to search, the value of the next item, and a left and right index
def binary_search(search_list, next_item, left, right):
    # If the index of left and right are the same, then the search has converged.
    if left == right:
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
    # Make the global  variable insertions available in this function
    global insertions
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
        # Increment insertions to keep track of how many green bars we want in the image (to show the length of
        # the sorted sublist)
        insertions += 1
        # Runs the save_image function for this step in the sorting process
        save_image(sort_list, insert_position)
    # Returns the sorted list
    return sort_list

# Function that saves 3 images to demonstrate how the sorting process works
# Accepts the unsorted list and the insertion_position
def save_image(unsorted_list, insertion_position):
    # Makes the global variables insertions, images, and image_counter available
    # to the function
    global insertions
    global images
    global image_counter

    # The first image is to show the newly inserted item, with previously sorted
    # items rendered as green.
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
    plt.title("Binary Insertion Sort")

    # Color all the bars in the sorted sublist (the length of insertions) green
    for j in range(0, insertions+1, 1):
        bars[j].set_color('g')
    # Color the newly inserted bar yellow
    bars[insertion_position].set_color('y')

    # Save the figure with a file name based on the image counter
    plt.savefig(f'binary_insertion_sort_images_2/{image_counter}.png')
    # Add the newly created filename to the list of image names for later gif creation
    image_names.append(f'binary_insertion_sort_images_2/{image_counter}.png')
    # Increment image counter
    image_counter += 1

    # This saves another image using the same idea as the above image code, 
    # but with all of the sorted sublist colored green. 
    # Visually this communicates to the viewer the insertion is complete.
    plt.clf()
    x_pos = np.arange(len(unsorted_list))
    height = unsorted_list

    bars = plt.bar(x_pos, height, width = 0.6)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title("Binary Insertion Sort")

    # The only difference is that we don't color the newly inserted bar yellow.
    for j in range(0, insertions+1, 1):
        bars[j].set_color('g')
    
    plt.savefig(f'binary_insertion_sort_images_2/{image_counter}.png')
    image_names.append(f'binary_insertion_sort_images_2/{image_counter}.png')
    image_counter += 1

    # This saves another image using the same idea as the above image code,
    # but with the sorted sublist colored green AND the next item to be compared
    # colored red.
    # This communicates to the viewer that the next item is the one being compared

    # If the insertions have reached the end of the list then there is no next item 
    # to be compared, so don't run the code.
    if insertions < list_length-1:
        plt.clf()
        x_pos = np.arange(len(unsorted_list))
        height = unsorted_list

        bars = plt.bar(x_pos, height, width = 0.6)
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title("Binary Insertion Sort")

        for j in range(0, insertions+1, 1):
            bars[j].set_color('g')
        # The difference here is that the next item is colored red.
        bars[insertions+1].set_color('r')

        plt.savefig(f'binary_insertion_sort_images_2/{image_counter}.png')
        image_names.append(f'binary_insertion_sort_images_2/{image_counter}.png')
        image_counter += 1

# Main user interface code, to ask how many items should be sorted
list_length = int(input('How many items would you like to sort? \n'))
# Creates an unsorted list with as many unique integer values as the number of items to be sorted
# Basically, if the user enters 100, there will be values from 1-101 just randomly ordered.
unsorted_list = rand.sample(range(1,list_length+1),list_length)

# Saves an initial image because a value hasn't been sorted yet.
plt.clf()
x_pos = np.arange(len(unsorted_list))
height = unsorted_list

bars = plt.bar(x_pos, height, width = 0.6)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title("Binary Insertion Sort")

for j in range(0, insertions+1, 1):
    bars[j].set_color('g')
# Colors the next value to be sorted red
bars[insertions+1].set_color('r')

plt.savefig(f'binary_insertion_sort_images_2/base.png')
image_names.append(f'binary_insertion_sort_images_2/base.png')
image_counter += 1

# Runs the insertion sort on the unsorted list and assigns the output to
# sorted_list
sorted_list = insertion_sort(unsorted_list)

# Displays the unsorted and sorted lists.
print(f'first unsorted list: {unsorted_list} \n')

print(f'final sorted list: {sorted_list} \n')

# Code the creates the GIF.
# For loop iterates through the list of image names, reads the data at each file path,
# And appends the data to the images array. 
for image_name in image_names:
    images.append(imageio.imread(image_name))
# The imageio uses the images array to feed data into the binary_insertion_sort.gif file,
# and loops it only once so that the user can see when the array is finished sorting.
imageio.mimwrite('binary_insertion_sort.gif', images, format ='GIF-FI', loop = 1, fps = 10)

