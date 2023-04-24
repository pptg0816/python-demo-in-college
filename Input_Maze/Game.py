import CreateMaze

while True:
    print('please input the size of maze,which should be an integer larger than 10:')
    try:
        size = int(input())
        if size < 10:
            print("too small")
        else:
            map_data = CreateMaze.create_maze(size)
            break
    except ValueError:
        print('invalid input')

# define the start and end point(start (1,1); end(size-2, size -2) )
x = 1
y = 1
endx = size - 2
endy = size - 2
map_data[x][y] = 2


# draw the map
# # means block
# ' 'means empty
# $ means current postion
def print_map():
    for nums in map_data:
        for num in nums:
            if num == 1:
                print(" #", end=" ")
            elif num == 0:
                print("  ", end=" ")
            else:
                print('\033[34m' + " $" + '\033[0m', end=" ")
        print("")


# print("original map")
# print_map()
# map_data[2][1], map_data[2+1][1] = map_data[2+1][1], map_data[2][1]
# print("map after moving")
# print_map()


print_map()
while True:
    #  move command
    order = input("input to move（a: left，s: down， d: right, w: up）：")

    # if left ( colum_index - 1 )
    if order == "a":
        y = y - 1
        # next step is block, game over
        if map_data[x][y] == 1:
            print("game over")
            break
        else:
            map_data[x][y], map_data[x][y + 1] = map_data[x][y + 1], map_data[x][y]  # swap
            print_map()

    # if down（ row_index + 1 ）
    elif order == "s":
        x = x + 1
        if map_data[x][y] == 1:
            print("game over")
            break
        else:
            map_data[x][y], map_data[x - 1][y] = map_data[x - 1][y], map_data[x][y]  # 进行交换操作
            print_map()

    # if right（ colum_index - 1 ）
    elif order == "d":
        y = y + 1
        if map_data[x][y] == 1:
            print("game over")
            break
        else:
            map_data[x][y], map_data[x][y - 1] = map_data[x][y - 1], map_data[x][y]  # 进行交换操作
            print_map()
            if map_data[x][y] == map_data[endx][endy]:
                print("congratulation!")
                break

    # if down（ row_index - 1 ）
    elif order == "w":
        x = x - 1
        if map_data[x][y] == 1:
            print("game over")
            break
        else:
            map_data[x][y], map_data[x + 1][y] = map_data[x + 1][y], map_data[x][y]  # 进行交换操作
            print_map()

    # deal invalid input
    else:
        print("invalid input! Please input again")
        continue
