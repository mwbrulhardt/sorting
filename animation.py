import os
import shutil

import imageio as imo
import matplotlib.pyplot as plt


def arrays_2_images(arrays, title, frame_path='data/'):
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


def array_2_barplot(x, y, title, path='/array.png'):
    plt.clf()
    plt.bar(x, y)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.savefig(path)


def images_2_gif(frames, path=''):

    with imo.get_writer(path + '.gif', mode='I') as writer:
        for frame in frames:
            image = imo.imread(frame)
            writer.append_data(image)


def arrays_2_gif(arrays, title='', path='', frame_path=''):
    images = arrays_2_images(arrays, title=title, frame_path=frame_path)
    images_2_gif(images, path=path)
    clear_folder(folder=frame_path)


def clear_folder(folder=None):

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)



