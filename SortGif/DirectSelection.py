import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import imageio


def RunDiectSelection(n):
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
            # use recursion delete function to delete all file in 'path' and the create it safely
            shutil.rmtree(path)
            os.mkdir(path)

    size = n
    path = './PNG'
    algorithmname = 'Direct'
    Xs = list(range(size))
    A = np.random.randint(-100, 100, size)

    checkfile(path)

    PNGLIST = []

    i, j, times = 0, 0, 0
    PNGLIST.append(os.path.join(path, str(times) + '.png'))
    times += 1
    plotAndSave(Xs, A, PNGLIST[-1])

    # DirectSelection Sort
    while i < size - 1:
        j = i+1
        while j < size:
            if A[i] > A[j]:  # if A[j] < A[i], swap
                A[j], A[i] = A[i], A[j]

                PNGLIST.append(os.path.join(path, str(times) + '.png'))
                plotAndSave(Xs, A, PNGLIST[-1])
                times += 1
            j += 1

        i += 1

    PNGLIST.append(os.path.join(path, str(times) + '.png'))
    plotAndSave(Xs, A, PNGLIST[-1])
    generated_images = []
    for png_path in PNGLIST:
        generated_images.append(imageio.imread(png_path))
    shutil.rmtree(path)

    imageio.mimsave(algorithmname + '.gif', generated_images, 'GIF', duration=0.1)