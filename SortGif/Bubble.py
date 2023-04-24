import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import imageio


def RunBubble(n):
    # pyplot
    # cla to clear current axis
    # bar to set a new axis with given X and Y
    # save the build axis to given path
    def plotAndSave(X, Y, path):
        plt.cla()
        plt.bar(X, Y)
        plt.savefig(path)


    def checkfile(path):
        if not os.path.exists(path):
            # create 'path' catalogue
            os.mkdir(path)
        else:
            # use recursion delete function to delete all file in 'path' and then create it safely
            shutil.rmtree(path)
            os.mkdir(path)

    size = n  # the size n defines how many random int number would you create in the axis
    path = './PNG'
    algorithmname = 'Bubble'
    Xs = list(range(size))  # build X with n size to store n random numbers
    A = np.random.randint(-100, 100, size)  # create n random numbers between -100 and 100. Return an array

    checkfile(path)

    PNGLIST = []

    i, j, times = 0, 0, 0
    PNGLIST.append(os.path.join(path, str(times) + '.png'))
    times += 1

    # at the beginning, output a
    plotAndSave(Xs, A, PNGLIST[-1])
    while i < size - 1:
        j = 0
        while j < size - 1 - i:
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                #if times % 3 == 0:
                PNGLIST.append(os.path.join(path, str(times) + '.png'))
                plotAndSave(Xs, A, PNGLIST[-1])

                times += 1
            j += 1
        i += 1

    # the last png in path
    PNGLIST.append(os.path.join(path, str(times) + '.png'))
    plotAndSave(Xs, A, PNGLIST[-1])

    generated_images = []
    for png_path in PNGLIST:
        # read every png in PNGLIST
        generated_images.append(imageio.imread(png_path))
    # remove 'path' that is useless
    shutil.rmtree(path)

    # use mimsave to build a gif, duration means seconds between every frames
    imageio.mimsave(algorithmname + '.gif', generated_images, 'GIF', duration=0.1)
