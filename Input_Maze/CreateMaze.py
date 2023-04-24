import random


def create_maze(size):
    # create a maze(size*size) and all its elements are "blocks" at the beginning
    # for each position, 1 means "block", 0 means "empty"
    map = [[] for i in range(size)]
    row = 0
    while row < size:
        count = 0
        while count < size:
            map[row].append(1)
            count += 1
        row += 1

    # remake the maze to set "start", "end" and "empty space"
    row = 0
    while row < size:
        col = 0
        while col < size:
            # set (1,1) as "start"
            if row == 1 and col == 1:
                map[row][col] = 0
            # set (size-2, size-2) as "end"
            elif row == size - 2 and col == size - 2:
                map[row][col] = 0
            # use random to create random empty spce at other position
            elif row != 0 and row != size - 1 and col != 0 and col != size - 1:
                map[row][col] = random.randint(0, 1)  # use randint to set (0,1) to each element randomly
            col += 1
        row += 1
    return map

