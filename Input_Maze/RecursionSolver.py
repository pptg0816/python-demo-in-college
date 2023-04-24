import CreateMaze

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # define four directions
path = []  # store the path


def mark(maze, pos):  # set 2 for the position which means have been here
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):  # check pos is 'empty' or 'block'
    return maze[pos[0]][pos[1]] == 0


def dfs_RecursionPath(maze, pos, end):
    mark(maze, pos)

    if pos == end:
        print(pos, end=" ")  # reach the end position, print it, append it to the path[] and return True
        # this is also the end condition of recursion
        path.append(pos)
        return True

    for i in range(4):  # check four direction in dirs, if one direction is not 'empty' at next step,
        # the for loop would change i, which means change another direction
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]

        if passable(maze, nextp):  # check is next step empty or not
            if dfs_RecursionPath(maze, nextp, end):  # use recursion here, until next step is "end".
                # If there is no way to get 'end', return False
                print(pos, end=" ")
                path.append(pos)
                return True

    return False


def see_path(maze, size, path):  # show the path
    # $ means the solved_path
    # * means have been here but get back to find another way
    # S means start
    # E means end
    # # means block
    # ' 'means empty
    for i, p in enumerate(path):
        maze[p[0]][p[1]] = 3
    maze[1][1] = "S"
    maze[size - 2][size - 2] = "E"
    print("\n")
    for r in maze:
        for c in r:
            if c == 3:
                print('\033[34m' + " $" + '\033[0m', end=" ")  # \033[xxm means set color. [0m means drop the color
            elif c == "S":
                print('\033[32m' + " S" + '\033[0m', end=" ")
            elif c == "E":
                print('\033[32m' + " E" + '\033[0m', end=" ")
            elif c == 2:
                print('\033[33m' + " *" + '\033[0m', end=" ")
            elif c == 1:
                print(" #", end=" ")
            else:
                print("  ", end=" ")
        print()


def draw_maze(maze):
    print("\n")
    # # means block
    # ' 'means empty
    for r in maze:
        for c in r:
            if c == 3:
                print('\033[34m' + " $" + '\033[0m', end=" ")
            elif c == "S":
                print('\033[32m' + " S" + '\033[0m', end=" ")
            elif c == "E":
                print('\033[32m' + " E" + '\033[0m', end=" ")
            elif c == 2:
                print('\033[33m' + " *" + '\033[0m', end=" ")
            elif c == 1:
                print(" #", end=" ")
            else:
                print("  ", end=" ")
        print()


def recursionStarter():
    while True:
        print('This is the test to use Recursion DFS\n')
        print('please input to decide use the certain map or use random map: "1" means certain and "2" means random')
        try:
            choice = int(input())
            if choice == 2:
                print('please input the size of maze,which should be an integer larger than 10:')
                try:
                    size = int(input())
                    if size < 10:
                        print("too small")
                    else:
                        maze = CreateMaze.create_maze(size)
                        break
                except ValueError:
                    print('invalid input')

            elif choice == 1:
                size = 14
                maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
                break
            else:
                print("invalid input")
        except ValueError:
            print('invalid input')

    start = (1, 1)
    end = (size - 2, size - 2)
    draw_maze(maze)
    if dfs_RecursionPath(maze, start, end):
        print('\nfind a way')
        see_path(maze, size, path)
        print('\n\n')
    else:
        print('no way')
        print('\n\n')

# recursionStarter()
