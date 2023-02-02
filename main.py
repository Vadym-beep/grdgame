#Setup grid
x, y = 5, 5
gridline = []
for i in range(x):
    gridline.append(0)
grid = []
for i in range(y):
    grid.append(list(gridline))


def setgridpoint(x, y, value):
    grid[y][x] = value
    



print(grid)