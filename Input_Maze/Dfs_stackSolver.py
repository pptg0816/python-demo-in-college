import CreateMaze


class Stack:
    def __init__(self):
        self.__data = []

    def is_empty(self):
        """check is the stack empty or not"""
        return self.__data == []

    def push(self, data):
        """add the element on the top of stack"""
        self.__data.append(data)

    def pop(self):
        """pop the element on the top of stack """
        return self.__data.pop()

    def peek(self):
        """return the element on the top of stack"""
        # 先判断是否为空
        if self.is_empty():
            return
        else:
            return self.__data[-1]

    def size(self):
        """return the size of stack"""
        return len(self.__data)

    def travel(self):
        """reverse the stack（which make it looks like 'pushing first, popping last') and return it"""
        self.__data = self.__data[::-1]
        p = []
        for i in self.__data:
            p.append(i[0])
        return p


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # define four directions


def mark(maze, pos):  # set 2 for the position which means have been here
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):  # check pos is 'empty' or 'block'
    return maze[pos[0]][pos[1]] == 0


def maze_solver(maze, start, end):
    st = Stack()
    if start == end:
        st.push((start, 0))
        print(start)
        return st.travel()
    mark(maze, start)
    st.push((start, 0))  # push start to stack as the first node
    while not st.is_empty():
        pos, nxt = st.pop()  # if stack is not empty, back up and find a new direction
        # nxt means next direction, which is in [0,3]
        for i in range(nxt, 4):  # check four direction in dirs, if one direction is not 'empty' at next step,
            # the for loop would change i, which means change another direction
            nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            if nextp == end:
                st.push((pos, 0))
                return st.travel()  # output the solved_path
            if passable(maze, nextp):  # check next step is empty or not
                st.push((pos, i + 1))  # push position and new direction
                mark(maze, nextp)  # mark next step as "have been here"
                st.push((nextp, 0))  # push
                break  # break inner loop and try another direction and use new position as the peek of stack

    return st.travel()


def see_path(maze, size, path):  # see the path
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
solved_path = maze_solver(maze, start, end)

for node in solved_path:
    print(node[0])
see_path(maze, solved_path)
'''


def DfsStarter():
    while True:
        print('This is the test to use Stack DFS\n')
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
    solved_path = maze_solver(maze, start, end)
    if not solved_path:
        print('no way')
        print('\n\n')
    else:
        print('find a way')
        print(solved_path)
        see_path(maze, size, solved_path)
        print('\n\n')




