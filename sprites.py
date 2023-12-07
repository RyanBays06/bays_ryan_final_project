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

def fire(self, fire):
        self.fire = fire
        self.countdown.event_time = floor(pg.time.get_ticks()/1000)
        mpos = pg.mouse.get_pos()
        targetx = mpos[0]
        targety = mpos[1]
        distance_x = targetx - self.rect.x
        distance_y = targety - self.rect.y
        angle = atan2(distance_y, distance_x)
        speed_x = 10 * cos(angle)
        speed_y = 10 * sin(angle)
        # print(speed_x)
        if self.countdown.delta > 5:
            f = Bullet(self.pos.x,self.pos.y - self.rect.height, 30, 30, speed_x, speed_y, "player")
            self.all_sprites.add(f)
            self.all_bullets.add(f)
        elif self.countdown.delta > .2:
            f = Bullet(self.pos.x,self.pos.y - self.rect.height, 10, 10, speed_x, speed_y, "player")
            self.all_sprites.add(f)
            self.all_bullets.add(f)
            print(self.countdown.delta)
        keys = pg.key.get_pressed()
        if keys[pg.K_b]:
            self.fire
        
    


class Alien(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
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
    def __init__(self, x, y, w, h,sx,sy, owner):
        Sprite.__init__(self)
        self.owner = owner
        self.image = pg.Surface((w, h))
        self.image = pg.image.load(os.path.join(img_folder, 'bulletspaceinvaders.jpg')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        if self.owner == 'player':
            self.radius = w/2
        else:
            self.image.fill(RED)
        self.rect.x = x
        self.rect.y = y
        self.speed_x = sx
        self.speed_y = sy
        self.fired = False
    
    def update(self):
        if self.owner == "player":
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
           
        else:
            self.rect.y += self.speed_y
        if (self.rect.y < 0 or self.rect.y > HEIGHT):
            self.kill()
            


                

    def update(self):
        pass


     
       
      
       
        
       
        
