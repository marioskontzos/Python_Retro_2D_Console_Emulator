import pygame
import os
import sys
import time
import random
from Objectives import *

sys.path.append('C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/')
path = 'C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/Sound_Images/'

class snake_Body(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height, colour, body_type):
        super().__init__()

        self.speedx = 30
        self.speedy = 0
        self.width = 30
        self.height = 30
        self.original_length = 3
        self.display_width = display_width
        self.display_height = display_height
        self.colour = colour
        self.rotation = 1      
        self.x = (self.display_width / 2) - self.width
        self.y = (self.display_height / 2)
        self.image = pygame.image.load(path + 'Snake_Body_30x30.png').convert()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.image.set_colorkey(self.colour)
        self.body_type = body_type
        self.set_Init_Position()  
        self.set_Image()

    def set_Direction(self, x, y, r):
        self.speedx = x
        self.speedy = y
        self.rotation = r
          
        #Check window boundaries
        if (-self.width > self.rect.x)  or (self.rect.x > self.display_width +5) or (self.rect.y < -self.height) or (self.rect.y > self.display_height +5):
            self.alive = 0

    def Reposition(self, listx, listy):
        self.rect.x = listx
        self.rect.y = listy
    
    def set_Rotation(self, r):
        self.rotation = r

    def set_Init_Position(self):
        if self.body_type == 1:
            self.x = (self.display_width / 2) - self.width
            self.y = (self.display_height / 2)
        else:
            self.x = -self.width
            self.y = -self.height
        self.image = pygame.image.load(path + 'Snake_Body_30x30.png').convert()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.image.set_colorkey(self.colour)

    def set_Image(self):
        self.image = pygame.image.load(path + 'Snake_Body_30x30.png').convert()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.image.set_colorkey(self.colour)

class snake_Head(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height, colour):
        super().__init__()

        self.speedx = 30
        self.speedy = 0
        self.width = 30
        self.height = 30
        self.original_length = 3
        self.display_width = display_width
        self.display_height = display_height
        self.colour = colour
        self.rotation = 1
        self.alive = 1
        self.points = 0
        self.swap = 1
        self.swapTimer = 0.0       
        self.x = (self.display_width / 2)
        self.y = (self.display_height / 2)
        self.image = pygame.image.load(path + 'Snake_Head_New_Right_30x30.png').convert()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.image.set_colorkey(self.colour)
        self.body_type = 1
        self.set_Init_Position()  
        self.set_Image()

    def set_body_type(self, t):
        self.body_type = t

    def set_Direction(self, x, y, r):
        self.speedx = x
        self.speedy = y
        self.rotation = r

    def move(self):
        if self.speedx > 0 or self.speedx < 0:
            self.rect.x += self.speedx
            self.x = self.rect.x
        else:
            self.rect.y += self.speedy
            self.y = self.rect.y
          
        #Check window boundaries
        if (-self.width > self.rect.x)  or (self.rect.x > self.display_width +5) or (self.rect.y < -self.height) or (self.rect.y > self.display_height +5):
            self.alive = 0
        self.set_Image()

    def Reposition(self, listx, listy):
        self.rect.x = listx
        self.rect.y = listy
    
    def set_Rotation(self, r):
        self.rotation = r

    def set_Init_Position(self):
        self.x = (self.display_width / 2)
        self.y = (self.display_height / 2)
        self.image = pygame.image.load(path + 'Snake_Head_New_Right_30x30.png').convert()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.image.set_colorkey(self.colour)

    def set_Image(self):
        if self.rotation == 1:
            self.image = pygame.image.load(path + 'Snake_Head_New_Right_30x30.png').convert()
            self.rect = self.image.get_rect(topleft = (self.x, self.y))
            self.image.set_colorkey(self.colour)
        elif self.rotation == 2:
            self.image = pygame.image.load(path + 'Snake_Head_New_Left_30x30.png').convert()
            self.rect = self.image.get_rect(topleft = (self.x, self.y))
            self.image.set_colorkey(self.colour)
        elif self.rotation == 3:
            self.image = pygame.image.load(path + 'Snake_Head_New_Up_30x30.png').convert()
            self.rect = self.image.get_rect(topleft = (self.x, self.y))
            self.image.set_colorkey(self.colour)
        else:
            self.image = pygame.image.load(path + 'Snake_Head_New_Down_30x30.png').convert()
            self.rect = self.image.get_rect(topleft = (self.x, self.y))
            self.image.set_colorkey(self.colour)

def fruit_collision(snake_head_List, objective_list, all_sprites_list):
    k = 0
    for snake_head in snake_head_List:
        objective_snake_collide_list = pygame.sprite.spritecollide(snake_head, objective_list, False)
        if objective_snake_collide_list:
            for fruit in objective_list:
                fruit.respawn()
                k = fruit.points
    return k