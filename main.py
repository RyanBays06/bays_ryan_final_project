# This file was created by Ryan Bays 11/27/23

# PROJECT GOALS
   # Create a game where the player has to do two tasks at once, like space invaders
   # Make mobs respawn after they are all killed
   # Create a player that can fire rockets/bullets to destroy obstacles
   # Be able to collect points for killing mobs

# SOURCES
   # Chris Cozort mygame base code
   # [NPStation](https://www.youtube.com/watch?v=UHBk_qDY4JE)




# import libraries and modules
import turtle 
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math


vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self): 
        # create a group for all sprites
        self.bgimage = pg.image.load(os.path.join(img_folder, 'galaxybg1.png')).convert()
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_bullets = pg.sprite.Group()
        self.all_aliens = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)
    

        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for a in range(0,25):
            a = Alien(randint(0, WIDTH), randint(0, math.floor(HEIGHT/2)), 20, 20, "moving")
            self.all_sprites.add(a)
            self.all_aliens.add(a)
        
        if self.all_aliens == 0:
           self.all_aliens += 10
        
        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        if self.player.pos.x < 0:
            self.player.pos.x = WIDTH
        if self.player.pos.x > WIDTH:
            self.player.pos.x = 0        
        
        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y >= 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed*1.5

                    
         # this prevents the player from jumping up through a platform
        elif self.player.vel.y <= 0:
            hits = pg.sprite.spritecollide(self.player, False)
            if hits:
                self.player.acc.y = 5
                self.player.vel.y = 0

            hits = pg.sprite.spritecollide(self.all_bullets, self.all_aliens, True)
            if hits:
                self.score += 1

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONUP:
               # player.fire()
               self.player.vert_fire() 
            
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        self.screen.blit(self.bgimage,(0,0))
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Hitpoints: " + str(self.player.hitpoints), 22, WHITE, WIDTH/2, HEIGHT/10)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/7)
        # buffer - after drawing everything, flip display
        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
        

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

        
       
        
    
 
           

g = Game()
while g.running:
    g.new()



pg.quit()


