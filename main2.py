x, y = 5, 5
gridline = []
for i in range(x):
    gridline.append(0)
grid = []
for i in range(y):
    grid.append(list(gridline))
grid[0][0] = 1
print(grid)
