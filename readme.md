**#Grdgame**

Grdgame (codenamed langfromnotebook) is a game which was intended to be a programming language, as its name tells you, the ideas for it are in my notebook.
Grdgame is a challenge for your eyes to find the ending point which is marked 3 and move to it.
This game is a command line game, where you can see a grid of numbers:
0 = empty
1 =  starting point
2 =  current point
3 =  ending point
To move your current point you have to use the `move` command and supply how many spaces you want to move in the x direction (to the right) and in the y direction (down)
like this: `move 3 2`
You can also supply negative numbers to move in the opposite direction 
like this: `move -1 0`
this will move you to the left 1 space.
After you have reached the ending point and the 3 on the grid has been replaced by 2, type the `end` command, and if `True` appears on the terminal, you have won.
If `False` appears you have lost.

Both the `main.py` file and the `config.py` file is necessary for the game to work, to launch the game, clone the repo, and type `python3 main.py`.

This game is currently in development and created by Vadym-beep.
