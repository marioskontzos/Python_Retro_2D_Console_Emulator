import os,sys,pygame,random,time

sys.path.append('C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/')
path = 'C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/Sound_Images/'

class Objectives(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height):
        super().__init__()

        self.size = 30
        self.points = 1
        self.display_width = display_width
        self.display_height = display_height
        self.x = random.randrange(self.size, self.display_width - self.size)
        self.y = random.randrange(self.size, self.display_height - self.size)

    def respawn(self):
        self.rect.x = random.randrange(self.size, self.display_width - self.size)
        self.rect.y = random.randrange(self.size, self.display_height - self.size)

    def set_Image(self, x, colour):
        if x == 1:
            self.image = pygame.image.load(path + 'apple_30x30.png').convert()
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.image.set_colorkey(colour)
        elif x == 2:
            self.image = pygame.image.load(path + 'Human_Standing_2_97x115.png').convert()
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.image.set_colorkey(colour)
            self.speedx = 0
            self.speedy = 0
            self.swap = 1
            self.swapTimer = 0.0

    def swap_Image(self):
        self.x = self.rect.x
        self.y = self.rect.y
        if time.time() - self.swapTimer > 0.035:
            if self.swap == 1:
                if self.rotation == 1:
                    self.image = pygame.image.load(path + 'Human_Move_2_97x115.png').convert()
                    self.rect = self.image.get_rect(topleft = (self.x, self.y))
                    self.image.set_colorkey(self.colour)
                elif self.rotation == 2:
                    self.image = pygame.image.load(path + 'Human_Move_2_97x115.png').convert()
                    self.rect = self.image.get_rect(topleft = (self.x, self.y))
                    self.image.set_colorkey(self.colour)
                elif self.rotation == 3:
                    self.image = pygame.image.load(path + 'Human_Move_2_97x115.png').convert()
                    self.rect = self.image.get_rect(topleft = (self.x, self.y))
                    self.image.set_colorkey(self.colour)
                elif self.rotation == 4:
                    self.image = pygame.image.load(path + 'Human_Move_2_97x115.png').convert()
                    self.rect = self.image.get_rect(topleft = (self.x, self.y))
                    self.image.set_colorkey(self.colour)
                self.swap = 0
            elif self.swap == 0:
                if self.rotation == 1:
                    self.image = pygame.image.load(path + 'Human_Standing_2_97x115.png').convert()
                    self.rect = self.image.get_rect(topleft = (self.x, self.y))
                    self.image.set_colorkey(self.colour)
                elif self.rotation == 2:
                    self.image = pygame.image.load(path + 'Human_Standing_2_97x115.png').convert()
                    self.rect = self.image.get_rect(topleft = (self.x, self.y))
                    self.image.set_colorkey(self.colour)
                elif self.rotation == 3:
                    self.image = pygame.image.load(path + 'Human_Standing_2_97x115.png').convert()
                    self.rect = self.image.get_rect(topleft = (self.x, self.y))
                    self.image.set_colorkey(self.colour)
                elif self.rotation == 4:
                    self.image = pygame.image.load(path + 'Human_Standing_2_97x115.png').convert()
                    self.rect = self.image.get_rect(topleft = (self.x, self.y))
                    self.image.set_colorkey(self.colour)
                self.swap = 1
            self.swapTimer = time.time()