from pprint import pprint
import config
import sys
startpoint = config.startpoint
currentpoint = startpoint
endpoint = config.endpoint
x = config.x
y = config.y

gridline = []
for i in range(x):
    gridline.append(0)
grid = []
for i in range(y):
    grid.append(list(gridline))


def setgridpoint(x, y, value):
    grid[y][x] = value
    
def move(x, y):
        global currentpoint
        grid[currentpoint[1]][currentpoint[0]] = 0
        currentpoint[0] += x
        currentpoint[1] += y
        grid[currentpoint[1]][currentpoint[0]] = 2
        print(currentpoint)
def end():
    global currentpoint
    global endpoint
    endpoint[1] -= endpoint[1]+endpoint[1]+1 # Fixes the endpoint coordinates to coreespond with the technical grid coordinates.
    print(currentpoint)
    print("\n================================\n")
    print(endpoint)
    if currentpoint[0] == endpoint[0] and currentpoint[1] == endpoint[1]:
        return True
    else:
        return False

setgridpoint(startpoint[0], startpoint[1], 1)
setgridpoint(endpoint[0], endpoint[1], 3)
grid.reverse()
# Points:
# 1 =  startpoint
# 2 =  currentpoint
# 3 =  endpoint
# 4 =  PlantedCmd
######################
from cmd import Cmd
class MyPrompt(Cmd):
    prompt = 'grdgame -+> '

    def do_move(self, inp):
        coords = inp.split()
        x = int(coords[0])
        y = int(coords[1])
        move(x, -y)
        pprint(grid)

    def do_end(self, inp):
        print(end())
        sys.exit(0)
    def do_pgrid(self, inp):
        pprint(grid)
######################
p = MyPrompt()
p.cmdloop()
grid.reverse()
print(end())
exit()
