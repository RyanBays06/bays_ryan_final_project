# This file was created by Ryan Bays 11/27/23

from random import randint 
import math

# game settings 
WIDTH = 1100
HEIGHT = 800
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal")]
ALIEN_LIST = [randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 20, 20, "moving"]