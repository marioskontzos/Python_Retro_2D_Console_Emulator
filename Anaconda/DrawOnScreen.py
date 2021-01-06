import pygame
import os, sys,time
import random

sys.path.append('C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/')
path = 'C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/Sound_Images/'

class DrawWindows(pygame.sprite.Sprite):
    def __init__(self, gameDisplay, display_width, display_height):
        super().__init__()
        
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.YELLOW = (255, 255, 0)
        self.gameDisplay = gameDisplay
        self.display_width = display_width
        self.display_height = display_height
        self.set_Image(1)

    def show_Screen(self):
        self.gameDisplay.blit(self.image, self.rect)
        self.draw_Text("Anaconda", 64, self.display_width / 2, self.display_height / 4)
        self.draw_Text("Arrow keys move", 22, self.display_width / 2 - 150, self.display_height / 2)
        self.draw_Text("Escape to exit", 22, self.display_width / 2 + 150, self.display_height / 2 )
        self.draw_Text("Press any key to begin", 18, self.display_width / 2, self.display_height * 3 / 4)

    def draw_Text(self, text, size, width, height):
        font = pygame.font.Font('freesansbold.ttf', size)
        text_surface = font.render(text, True, self.RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (width, height)
        self.gameDisplay.blit(text_surface, text_rect)

    def game_Over(self, text, size):
        font = pygame.font.Font('freesansbold.ttf', size)
        text_surface = font.render(text, True, self.RED)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.display_width / 2, self.display_height / 2)
        self.gameDisplay.blit(text_surface, text_rect)
        pygame.display.update() 
        time.sleep(3)
    
    def show_Background(self):
        self.gameDisplay.blit(self.image, self.rect)

    def set_Image(self, x):
        if x == 1:
            self.image = pygame.image.load(path + 'Snake_Background_1366x768.jpg').convert()
            #self.image = pygame.image.load(path + 'Snake_Background_1900x1080.jpg').convert()
            self.rect = self.image.get_rect()
        else:
            #self.image = pygame.image.load(path + 'Snake_Background_1366x768.jpg')
            self.image = pygame.image.load(path + 'Background_Ingame_1366x768.jpg')
            #self.image = pygame.image.load(path + 'Background_Ingame_1900x1080.jpg')
            self.imageRect = self.image.get_rect()