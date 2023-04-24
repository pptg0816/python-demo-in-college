import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import imageio

PNGLIST = []  # PNGlist to store sort of png and combine them as one gif
times = 0


def RunQuick(n):
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

    # A is the random array
    # s is start
    # e is end
    # in this qsort, I use A[s](k) as a symbol value.
    # Put all element that smaller than A[s](k) on its left side
    # Put all element that bigger than A[s](k) on its right side
    # Divide array as two part from A[s](k) and use recursion to do same operation on each side

    def qsort(A, s, e):
        global PNGLIST, times
        if s >= e:
            return None
        i, j, k = s, e, A[s]
        while i < j:
            while i < j and A[j] >= k:  # compare from end. If A[j] >= k, just check the next left element
                j -= 1
            if i < j:
                A[i] = A[j]  # until one A[j] < k, set k as it value

            while i < j and A[i] <= k:  # compare from start. If A[i] <= k, just check the next right element
                i += 1
            if i < j:
                A[j] = A[i]  # until one A[i] > k, set k as it value

        A[i] = k  # set k for the middle element after first sort loop

        PNGLIST.append(os.path.join(path, str(times) + '.png'))
        plotAndSave(Xs, A, PNGLIST[-1])
        times += 1

        qsort(A, s, i - 1)
        qsort(A, i + 1, e)

    global PNGLIST, times
    size = n
    path = './PNG'
    algorithmname = 'Quick'
    Xs = list(range(size))
    A = np.random.randint(-100, 100, size)

    checkfile(path)

    PNGLIST.append(os.path.join(path, str(times) + '.png'))
    plotAndSave(Xs, A, PNGLIST[-1])
    times += 1

    qsort(A, 0, size - 1)
    PNGLIST.append(os.path.join(path, str(times) + '.png'))
    plotAndSave(Xs, A, PNGLIST[-1])

    generated_images = []
    for png_path in PNGLIST:
        generated_images.append(imageio.imread(png_path))
    shutil.rmtree(path)

    imageio.mimsave(algorithmname + '.gif', generated_images, 'GIF', duration=0.5)
