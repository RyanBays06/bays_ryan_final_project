# This file was created by Ryan Bays 11/27/23

# import libraries and modules
# from platform import platform
from hashlib import new
from itertools import count
from secrets import choice
import pygame as pg
# import settings
from settings import *
from pygame.sprite import Sprite
import random
from random import randint, randrange
import os
from os import path
from math import *
from time import *

import turtle
import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # self.image = pg.Surface((50, 50))
        # self.image.fill(GREEN)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'spaceinvaderplayer1.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.hitpoints = 100
   # controls the movement of player
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        
    
    def update(self):
        # CHECKING FOR COLLISION WITH MOBS HERE>>>>>
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * -PLAYER_FRIC
        # self.acc.y += self.vel.y * -0.3
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
     # what makes the bullets fire from player
    def vert_fire(self):
        p = Bullet(self.game, self.pos.x,self.pos.y - self.rect.height, 30, 30)
        self.game.all_sprites.add(p)
        self.game.all_bullets.add(p)
    
  
       


class Alien(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        # appearance of aliens on screen
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.image = pg.image.load(os.path.join(img_folder, 'alienspaceinvmob.jpg')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed= 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            # Check to see if this thing is on one side of the screen or the other
            if self.rect.x > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
                self.rect.y -= self.rect.h           
          

class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        # platform at the bottom of the screen that keeps player on the screen
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0
        if self.category == "moving":
            self.speed = 5
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed

        
class Bullet(Sprite):
    def __init__(self, game, x, y, w, h):
        Sprite.__init__(self)
        # appearance of bullet/rocket on the screen
        self.game = game
        self.image = pg.Surface((w, h))
        self.image = pg.image.load(os.path.join(img_folder, 'bsi.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = w/2
        self.rect.x = x
        self.rect.y = y
        self.fired = False
        
    # kills bullet after it goes offscreen
    # makes mobs disappear when bullet hits them
    def update(self):
        self.rect.y -= 10
        hits = pg.sprite.spritecollide(self, self.game.all_aliens, True)
        if self.rect.y == -1:
            self.kill
        
        

            


     
       
      
       
        
       
        
