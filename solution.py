# 迷宫阵
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]
# 开始和结束
start_x, start_y = 1, 1
end_x, end_y = 5, 5


def find(x, y):
    # 当前搜过的置 2，就不要再搜了
    maze[x][y] = 2
    # 四个搜索方向
    r1, r2, r3, r4 = False, False, False, False
    # 如果到达了终止点，那就成功了
    if x == end_x and y == end_y:
        return 1
    # 搜索四个方向，并获取结果
    if maze[x + 1][y] == 0:
        r1 = find(x + 1, y)
    if maze[x][y + 1] == 0:
        r2 = find(x, y + 1)
    if maze[x - 1][y] == 0:
        r3 = find(x - 1, y)
    if maze[x][y - 1] == 0:
        r4 = find(x, y - 1)
    # 如果有一个成功了就成功了
    if r1 or r2 or r3 or r4:
        return 1
    # 如果都失败了，那么将路径置零
    else:
        maze[x][y] = 0


if __name__ == '__main__':
    find(1, 1)
    for item in maze:
        print(item)

'''
[1, 1, 1, 1, 1, 1, 1]
[1, 2, 0, 0, 0, 0, 1]
[1, 2, 1, 0, 1, 0, 1]
[1, 2, 2, 0, 0, 1, 1]
[1, 1, 2, 1, 0, 1, 1]
[1, 0, 2, 2, 2, 2, 1]
[1, 1, 1, 1, 1, 1, 1]
'''
