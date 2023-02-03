startpoint = [0,0]
endpoint = [5,5]
x, y = 10, 10
class PlantedCmd:
    def __init__(self, coords, cmd):
        self.coords = coords
        self.cmd = cmd
    def execute(self):
        exec(self.cmd)
pcmd1 = PlantedCmd([3,3], "exit()")
pcmds = []
pcmds.append(pcmd1)
