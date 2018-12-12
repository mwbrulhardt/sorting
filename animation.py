import os
import shutil
import imageio as imo
import matplotlib.pyplot as plt


def arrays_2_images(arrays: list, title: str, frame_path: str='data/') -> list:
    """Converts a list of arrays to a list of images.

    These are temporarily stored in the directory 'frame_path' and are created
    from the matplotlib library.

    Params:
        arrays (list[float or int]): a
        title: title of the matplotlib plot
        frame_path: directory in which the images will be stored.

    Return:
        images (list[str]): returns a list of filenames at which the images are located.
    """
    indices = range(len(arrays[0]))
    m = len(arrays)
    images = []
    for i in range(m):
        values = arrays[i]
        filename = 'frame_' + str(i) + '.png'
        path = frame_path + filename
        array_2_barplot(indices, values, title, path=path)
        images.append(path)
    return images


def array_2_barplot(x: list, y: list, title: str, path: str='/array.png') -> None:
    """Generates a barplot from an array and saves it in the given path.

    Given a list x and y values, a title of the plot, and a place to save the
    plot this function creates a barplot and saves it in the given path.

    Params:
        x (list[int or float]): a list of numbers for the x-axis
        y (list[int or float]): a list of numbers for the y-axis
        title (str): a title for the barplot
        path: a path to save the barplot to
    """
    plt.clf()
    plt.bar(x, y)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.savefig(path)


def images_2_gif(frames: list, path: str='') -> None:
    """Creates a gif from a list of images.

    Given a list of paths for frame files and a location to store the gif, this
    function creates a gif from the images and saves the gif to the argument
    'path'.

    Params:
        frames (list[str]): a list of filenames
        path: a path to save the gif to
    """
    with imo.get_writer(path + '.gif', mode='I') as writer:
        for frame in frames:
            image = imo.imread(frame)
            writer.append_data(image)


def arrays_2_gif(arrays: list, title: str='', path: str='', frame_path: str='') -> None:
    """Creates a gif out of a list of arrays.

    Given a list of arrays, a title, a path, and a frame path, this function
    creates a gif with the given title saved to the argument 'path' and uses
    the 'frame_path' argument to store temporary frames of the barplots for
    gif.

    Params:
        arrays (list[list[float or int]]): a list of arrays
        title: a title for the gif
        path: a path to save the gif to
        frame_path: a path to temporarily the frames for the gif.
    """
    images = arrays_2_images(arrays, title=title, frame_path=frame_path)
    images_2_gif(images, path=path)
    clear_folder(folder=frame_path)


def clear_folder(folder: str) -> None:
    """Clears an entire folder.

    Given a folder name, this function will delete all the files that are in
    that folder.

    Params:
        folder (str): the path for the folder to be deleted.
    """

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
