#Setup grid
xRows, yColumns = 5, 5
grid = []
z = []
for j in range(xRows):
    z.append(0)
for i in range(yColumns):
    grid.append(z)


def setgridpoint(x, y, value):
    gridx = grid[x]
    gridx[y] = value


grid[0][0] = 1
print(grid)