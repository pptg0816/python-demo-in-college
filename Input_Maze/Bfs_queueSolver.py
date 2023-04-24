import CreateMaze


class Queue:
    def __init__(self):
        self.__data = []

    def enqueue(self, data):
        """add a new element at start of queue"""
        self.__data.insert(0, data)

    def travel(self):
        """output all data"""
        p = []
        for i in self.__data:
            p.append(i)
        return p

    def dequeue(self):
        """drop an old element at the end of queue"""
        return self.__data.pop()

    def is_empty(self):
        """Check is the queue empty"""
        return self.__data == []

    def size(self):
        """get the size of queue"""
        return len(self.__data)


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # define four directions


def mark(maze, pos):  # set 2 for the position which means have been here
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):  # check pos is 'empty' or 'block'
    return maze[pos[0]][pos[1]] == 0


def maze_solver_queue(maze, start, end):
    qu = Queue()
    if start == end:
        qu.enqueue(start)
        print(start)
        return qu.travel()
    mark(maze, start)
    qu.enqueue(start)  # put start in queue
    while not qu.is_empty():  # check is queue empty or not
        pos = qu.dequeue()  # pop the end of queue
        for i in range(4):  # check four direction in dirs, if one direction is not 'empty' at next step,
            # the for loop would change i, which means change another direction
            nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            if passable(maze, nextp):  # check next step is empty or not
                if nextp == end:  # if next step is "end"
                    qu.enqueue(pos)
                    print("find a way")
                    qu.enqueue(end)
                    return qu.travel()
                mark(maze, nextp)
                qu.enqueue(nextp)  # put the new element at the start of queue


def see_path(maze, size, path):  # see the maze
    for node in path:
        maze[node[0]][node[1]] = 3
    maze[1][1] = "S"
    maze[size - 2][size - 2] = "E"
    print("\n")
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


def draw_maze(maze):
    print("\n")

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


'''
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

start = (1, 1)
end = (size - 2, size - 2)
solved_path = maze_solver_queue(maze, start, end)

for node in solved_path:
    print(node)
see_path(maze, size, solved_path)
'''


def BfsStarter():
    while True:
        print('This is the test to use Queue BFS\n')
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
    solved_path = maze_solver_queue(maze, start, end)
    if not solved_path:
        print('no way')
        print('\n\n')
    else:
        print(solved_path)
        see_path(maze, size, solved_path)
        print('\n\n')


