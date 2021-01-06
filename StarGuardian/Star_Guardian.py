"""
Created on Wed Sep 19 11:29:24 2018

@author: marios
"""

import pygame
import os
import random
import time

#Graphics
os.environ['SDL_VIDEO_CENTERED'] = '1'

def start():
    # Colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW = (255, 255, 0)

    #Paths
    game_path = "C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/StarGuardian/"

    pygame.init()

    #Adapt Window Graphics
    info = pygame.display.Info()
    display_width = info.current_w
    display_height = info.current_h

    # Start Pygame
    #pygame.init()

    # Window Size and Name
    #display_height = 600

    #gameDisplay = pygame.display.set_mode((display_width,display_height),)
    #gameDisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
    pygame.display.set_caption("Star Guardian")

    # Window refresh rate
    FPS = 60
    clock = pygame.time.Clock()

    #Images

    #Hero Image
    spaceshipImgBee = pygame.image.load(game_path + 'Hero_Spaceship_Bee_65x63.png').convert()
    spaceshipRect = spaceshipImgBee.get_rect()

    spaceshipImgBeeFlame = pygame.image.load(game_path + 'Hero_Spaceship_Bee_Flame_65x63.png').convert()
    spaceshipFlameRect = spaceshipImgBeeFlame.get_rect()

    #Alien Images
    alienPrivateImg = pygame.image.load(game_path + 'Alien_Private_50x88.png').convert()
    privateRect = alienPrivateImg.get_rect()

    alienSergeantImg = pygame.image.load(game_path + 'Alien_Sergeant_50x88.png').convert()
    sergeantRect = alienSergeantImg.get_rect()

    alienCaptainImg = pygame.image.load(game_path + 'Alien_Captain_50x95.png').convert()
    captainRect = alienCaptainImg.get_rect()

    bossBatImg = pygame.image.load(game_path + 'Boss_Bat_80x135.png').convert()
    batImg = bossBatImg.get_rect()

    bossGeneralImg = pygame.image.load(game_path + 'Boss_GeneralOfArmy_120x119.png').convert()
    generalImg = bossGeneralImg.get_rect()

    #Background Images

    #backgCosmos = pygame.image.load(game_path + 'Background_Cosmos_700x600.jpg').convert()
    backgCosmos = pygame.image.load(game_path + 'Background_Cosmos_1366x768.jpg').convert()
    #backgCosmos = pygame.image.load(game_path + 'Background_Cosmos_1900x1080.jpg').convert()
    cosmos = backgCosmos.get_rect()

    #backgRepublic = pygame.image.load(game_path + 'Background_Republic_700x600.jpg').convert()
    backgRepublic = pygame.image.load(game_path + 'Background_Republic_1366x768.jpg').convert()
    republic = backgRepublic.get_rect()

    #backgThunderStorm = pygame.image.load(game_path + 'Background_ThunderStorm_700x600.jpg').convert()
    backgThunderStorm = pygame.image.load(game_path + 'Background_ThunderStorm_1366x768.jpg').convert()
    thunderstorm = backgThunderStorm.get_rect()

    #backgGalaxy = pygame.image.load(game_path + 'Background_Galaxy_Image_700x600.png').convert()
    backgGalaxy = pygame.image.load(game_path + 'Background_Galaxy_1366x768.jpg').convert()
    #backgGalaxy = pygame.image.load(game_path + 'Background_Galaxy_1900x1080.jpg').convert()
    galaxy = backgGalaxy.get_rect()

    #backgNormalStars = pygame.image.load(game_path + 'Background_Space_Stars_Image_700x600.png').convert()
    backgNormalStars = pygame.image.load(game_path + 'Background_Space_1366x768.jpg').convert()
    normalStars = backgNormalStars.get_rect()

    #backgStars = pygame.image.load(game_path + 'Background_Space_Stars_Image_700x600.png').convert()
    backgStars = pygame.image.load(game_path + 'Background_Stars_1366x768.jpg').convert()
    stars = backgStars.get_rect()

    backgPlanets = pygame.image.load(game_path + 'Background_Planets_1366x768.jpg').convert()
    republic = backgRepublic.get_rect()


    # Hero Guns
    fireLaserL1 = pygame.image.load(game_path + 'Laser_PL1_5x35.png').convert()
    fLaserL1 = fireLaserL1.get_rect()

    fireLaserL2 = pygame.image.load(game_path + 'Laser_PL2_20x35.png').convert()
    fLaserL2 = fireLaserL2.get_rect()

    fireLaserL3 = pygame.image.load(game_path + 'Laser_PL3_30x50.png').convert()
    fLaserL3 = fireLaserL3.get_rect()

    frostLaserL1 = pygame.image.load(game_path + 'Frost_Laser_PL1_4x35.png').convert()
    frLaserL1 = frostLaserL1.get_rect()

    frostLaserL2 = pygame.image.load(game_path + 'Frost_Laser_PL2_20x35.png').convert()
    frLaserL2 = frostLaserL2.get_rect()

    frostLaserL3 = pygame.image.load(game_path + 'Frost_Laser_PL3_30x50.png').convert()
    frLaserL3 = frostLaserL3.get_rect()

    bullets = pygame.image.load(game_path + 'Bullets_10x20.png').convert()
    bullet = bullets.get_rect()

    leftBullets = pygame.image.load(game_path + 'Bullets_10x20_Left.png').convert()
    leftBullet = leftBullets.get_rect()

    rightBullets = pygame.image.load(game_path + 'Bullets_10x20_Right.png').convert()
    rightBullet = rightBullets.get_rect()

    # Alien Guns
    alien_FireLaser = pygame.image.load(game_path + 'Alien_FireLaser_15x25.png').convert()
    alien_FrostLaser = pygame.image.load(game_path + 'Alien_FrostLaser_6x16.png').convert()

    #Drop - Power ups icons
    staminaIcon = pygame.image.load(game_path + 'Drop_Stamina_28x23.png').convert()
    stIcon = staminaIcon.get_rect()

    healIcon = pygame.image.load(game_path + 'Drop_Heal_28x23.png').convert()
    hlIcon = healIcon.get_rect()

    tenacityIcon = pygame.image.load(game_path + 'Drop_Tenacity_28x23.png').convert()
    tnctIcon = tenacityIcon.get_rect()

    nanoshellIcon = pygame.image.load(game_path + 'Drop_NanoShell_28x22.png').convert()
    nsIcon = tenacityIcon.get_rect()

    bulletIcon = pygame.image.load(game_path + 'Drop_Bullet_28x16.png').convert()
    bulIcon = bulletIcon.get_rect()

    frostLaserIcon = pygame.image.load(game_path + 'Drop_FrostLaser_28x26.png').convert()
    frLIcon = frostLaserIcon.get_rect()

    fireLaserIcon = pygame.image.load(game_path + 'Drop_FireLaser_28x12.png').convert()
    flIcon = fireLaserIcon.get_rect()

    #audio
    airborne = game_path + 'airborne.wav'
    deadlocked = game_path + 'deadlocked.wav'
    finalbattle = game_path + 'finalbattle.wav'

    # Classes
    class Player(pygame.sprite.Sprite):
        def __init__(self, dw, dh, w, h):
            super().__init__()
            
            self.health = 100
            self.stamina = 100
            self.lives = 5
            self.displayWidth = dw
            self.displayHeight = dh
            self.width = w
            self.height = h
            self.image = spaceshipImgBee
            self.x = (self.displayWidth/ 2)
            self.y = self.displayHeight
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.image.set_colorkey(WHITE)
            self.weapon = 1
            self.powerLevel = 1
            self.damage = 20
            self.double_damage = 0
            self.doubleDamageChance = 0 
            self.speedx = 7
            self.speedy = 7
            
            self.slowed = 0
            self.slowDuration = 0.0
            self.slowflag = 0
            
            self.dissablesTimer = 2.0
            
            #Up to 40% reduced slow duration
            self.tenacity = 0
            self.newTenacity = 0
            
            #Up to 70% reduced income damage
            self.nanoshell = 0

            self.swap = 1
            self.swapTimer = 0
            
            
        # Methods	
        def setPosx(self, x):
            self.rect.x = x
            
        def setPosy(self, y):
            self.rect.y = y
            
        def moveX(self, x):
            self.rect.x += (x * self.speedx)
            
        def moveY(self, y):
            self.rect.y += (y * self.speedy)
            
        def setWeapon(self, x):
            if self.weapon == x:
                if self.weapon == 1:
                    if self.powerLevel <3:
                        self.damage += 50
                        self.powerLevel += 1
                elif self.weapon == 2: 
                    if self.powerLevel < 3:
                        self.damage += 70
                        self.powerLevel += 1
                elif self.weapon == 3:
                    if self.powerLevel < 3:
                        self.damage += 125
                        self.powerLevel += 1
                else:
                    if self.doubleDamageChance == 0:
                        k = random.randrange(20, 101)
                        if k <= 20:
                            self.damage = self.damage * 2
                            self.double_damage = 1
            elif self.weapon !=x:
                self.weapon = x
                if x == 1:
                    self.damage = 20
                    self.powerLevel = 1
                elif x == 2:
                    self.damage = 40
                    self.powerLevel = 1
                elif x == 3:
                    self.damage = 100
                    self.powerLevel = 1
                self.doubleDamageChance = 0
                
        def update(self):
            if self.health <= 0:
                if self.lives > 0 :
                    self.health = self.stamina
                    self.x = self.displayWidth / 2
                    self.y = self.displayHeight
                    self.rect = self.image.get_rect(center = (self.x, self.y))
                    self.lives -= 1
                    
            #Check if speed slowed down by frost laser and calculate time
            if self.slowed == 1:
                self.speedx = 1
                self.speedy = 1
                if time.time() - self.slowDuration > 0.0 and self.slowflag == 0:
                    self.slowDuration = time.time()
                    self.slowflag = 1
                elif self.slowflag == 1:
                    if time.time() - self.slowDuration > self.dissablesTimer:
                        self.slowed = 0
                        self.speedx = 7
                        self.speedy = 7
                        self.slowflag = 0
                        
            #Check tenacity and reset timer for slow
            if self.newTenacity != self.tenacity:
                self.newTenacity = self.tenacity
                self.dissablesTimer = (self.dissablesTimer - (self.dissablesTimer * (self.tenacity / 100)))

            self.swapImage()

        #Image Swap
        def swapImage(self):
            x = self.rect.x
            y = self.rect.y
            if time.time() - self.swapTimer > 0.035:
                if self.swap == 1:
                    self.image = spaceshipImgBeeFlame
                    self.rect = self.image.get_rect(topleft = (x, y))
                    self.image.set_colorkey(WHITE)
                    self.swap = 0
                elif self.swap == 0:
                    self.image = spaceshipImgBee
                    self.rect = self.image.get_rect(topleft = (x, y))
                    self.image.set_colorkey(WHITE)
                    self.swap = 1
                self.swapTimer = time.time()

    #Class of aliens (3 types)
    class Aliens(pygame.sprite.Sprite):
        def __init__(self, dw, dh, w, h):
            self.display_width = dw
            self.display_height = dh
            self.width = w
            self.height = h
            
            super().__init__()
            
    #Class of alien Private (type1, easy)
    class AlienPrivate(Aliens):
        def __init__(self, dw, dh, w, h):
            super().__init__(dw, dh, w, h)
            
            self.image = alienPrivateImg
            self.x = random.randrange(50, self.display_width - self.width)
            self.y = random.randrange((10 * (-self.height)) + 20, -self.height *3)
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.image.set_colorkey(BLACK)
            self.weapon = 1
            self.damage = 50
            self.health = 50
            self.speedy = random.randrange(3, 5)
            self.speedx = random.randrange(-2, 2)
            self.shootChance = 0
            self.dropChance = 26
            self.slowed = 0
            self.slowDuration = 0.0
            self.slowflag = 0
            self.dissablesTimer = 2.0
        
        # Private moves top -> bottom    
        def update(self):
            
            #Check movement behavior
            self.rect.y += self.speedy
            if self.rect.y + self.height >= 0:
                self.rect.x += self.speedx
            
            #Check if died or goes off the display boundaries
            if self.health <= 0 or self.rect.y > self.display_height:
                self.kill()
            
            # Check for shooting
            if self.rect.y + (self.height / 2) >= 0:
                if self.rect.x > 0 and self.rect.x < self.display_width - (self.width / 2):
                    self.shootChance = random.randrange(1,81)
                    
            #Check if speed slowed down by frost laser and calculate time
            if self.slowed == 1:
                self.speedx = 1
                self.speedy = 1
                if time.time() - self.slowDuration > 0.0 and self.slowflag == 0:
                    self.slowDuration = time.time()
                    self.slowflag = 1
                elif self.slowflag == 1:
                    if time.time() - self.slowDuration > self.dissablesTimer:
                        self.slowed = 0
                        self.speedx = random.randrange(-2, 2)
                        self.speedy = random.randrange(2, 4)
                        self.slowflag = 0
                    
        def spawnDrop(self):
            k = random.randrange(1, 101)
            if k <= self.dropChance:
                return 1
            else:
                return 0

    #Class of alien Sergeant (type 2, easy - medium)
    class AlienSergeant(Aliens):
        def __init__(self, dw, dh, w, h):
            super().__init__(dw, dh, w, h)
            
            self.image = alienSergeantImg
            self.spawnSide = random.randrange(-1, 2)
            k = 0
            self.x = self.setSpawnSide(k)
            self.y = random.randrange(0, ((display_height/2) - self.height))
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.image.set_colorkey(BLACK)
            self.weapon = 2
            self.damage = 80
            self.health = 80
            self.speedx = 3
            self.rotation = (-1) * self.spawnSide
            self.shootChance = 0
            self.dropChance = 35
            self.slowed = 0
            self.slowDuration = 0.0
            self.slowflag = 0
            self.dissablesTimer = 2.0
        
        #Set the spawn side x coordinates
        def setSpawnSide(self, k):
            if self.spawnSide == -1:
                k = random.randrange((-1)*(10 * self.width), (-1) *(3 * self.width))
            elif self.spawnSide == 1 or self.spawnSide == 0:
                k = random.randrange(self.display_width + (3 * (self.spawnSide * self.width)), self.display_width + 100 +(10 * (self.spawnSide * self.width)))
            return k
                
        # Sergeant moves with sidesteps    
        def update(self):
            if self.rotation == 0:
                self.rotation = -1
            
            if self.rotation == 1 and self.rect.x <= 0:
                self.rect.x += (self.rotation * self.speedx)
            elif self.rotation == 1 and self.rect.x + self.width < self.display_width and self.rect.x > 0:
                self.rect.x += (self.rotation * self.speedx)
            elif self.rotation == 1 and self.rect.x + self.width >= self.display_width:
                self.rotation = -1
                self.rect.x += (self.rotation * self.speedx)
            elif self.rotation == -1 and self.rect.x > 0:
                self.rect.x += (self.rotation * self.speedx)
            elif self.rotation == -1 and self.rect.x <= 0:
                self.rotation = 1
                self.rect.x += (self.rotation * self.speedx)
            elif self.rotation == -1 and self.rect.x >= self.display_width:
                self.rect.x += (self.speedx * self.rotation)
            elif self.rotation == -1 and self.rect.x < self.display_width:
                self.rect.x += (self.speedx * self.rotation)
            
            #Check if speed slowed down by frost laser and calculate time
            if self.slowed == 1:
                self.speedy = 1
                if time.time() - self.slowDuration > 0.0 and self.slowflag == 0:
                    self.slowDuration = time.time()
                    self.slowflag = 1
                elif self.slowflag == 1:
                    if time.time() - self.slowDuration > self.dissablesTimer:
                        self.slowed = 0
                        self.speedx = 3
                        self.slowflag = 0
            
            #Relocate if die
            if self.health <= 0:
                self.kill()
                
            #Check fot shooting
            if self.rect.x + (self.width / 2) >= 0:
                if self.rect.x + self.width <= self.display_width:
                    self.shootChance = random.randrange(1, 111)
                    
        def spawnDrop(self):
            k = random.randrange(1, 101)
            if k <= self.dropChance:
                return 1
            else:
                return 0

    #Class of alien Captain (type 3, medium - hard)        
    class AlienCaptain(Aliens):
        def __init__(self, dw, dh, w, h):
            super().__init__(dw, dh, w, h)
            
            self.image = alienCaptainImg
            self.x = (self.display_width / 2) - (self.width / 2)
            self.y = random.randrange(10 * (-self.height),3 * (-self.height))
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.image.set_colorkey(BLACK)
            self.weaponType = 0
            self.damage = 100
            self.health = 120
            self.speedx = 3
            self.speedy = 3
            self.rotationx = 1
            self.rotationy = 1
            self.screenEnter = 0
            self.shootChance = 0
            self.kamikaze = 0
            self.kamikazeChance = 0
            self.dropChance = 46
            self.slowed = 0
            self.slowDuration = 0.0
            self.slowflag = 0
            self.dissablesTimer = 2.0
        
        # Captain moves both ways    
        def update(self):
            # Side steps logic
            if self.screenEnter == 1:
                if self.rotationx == 1 and (self.rect.x + self.width) < (self.display_width - (self.width / 2)):
                    self.rect.x += (self.rotationx * self.speedx)
                elif self.rotationx == 1 and (self.rect.x + self.width) > (self.display_width - (self.width / 2)):
                    self.rotationx = -1
                    self.rect.x += (self.rotationx * self.speedx)
                elif self.rotationx == -1 and (self.rect.x + self.width) < self.display_width and self.rect.x > 0:
                    self.rect.x += (self.rotationx * self.speedx)
                elif self.rotationx == -1 and self.rect.x <= 0:
                    self.rotationx = 1
                    self.rect.x += (self.rotationx * self.speedx)
                if self.kamikaze == 1:
                    self.speedx = 0
            
            # Forward steps logic
            if self.screenEnter == 0:
                if self.rect.y < 0:
                    self.rect.y += self.speedy
                    if self.rect.y >= 0:
                        self.screenEnter = 1
            else :
                if self.kamikaze == 0:            
                    if self.rotationy == 1 and (self.rect.y + self.height) < (self.display_height / 2):
                        self.rect.y += (self.rotationy * self.speedy)
                    elif self.rotationy == 1 and (self.rect.y + self.height) >= (self.display_height / 2):
                        self.rotationy = -1
                        self.rect.y += (self.rotationy * self.speedy)
                    elif self.rotationy == -1 and self.rect.y > 0:
                        self.rect.y += (self.rotationy * self.speedy)
                    elif self.rotationy == -1 and self.rect.y <= 0:
                        self.rotationy = 1
                        self.rect.y += (self.rotationy * self.speedy)
                elif self.kamikaze == 1:
                    self.speedy = 8
                    self.rect.y += self.speedy
                    
            #Check if speed slowed down by frost laser and calculate time
            if self.slowed == 1:
                self.speedx = 1
                self.speedy = 1
                if time.time() - self.slowDuration > 0.0 and self.slowflag == 0:
                    self.slowDuration = time.time()
                    self.slowflag = 1
                elif self.slowflag == 1:
                    if time.time() - self.slowDuration > self.dissablesTimer:
                        self.slowed = 0
                        self.speedx = 3
                        self.speedy = 3
                        self.slowflag = 0
            
            #Set weapon type, Captain fires both fire laser and frost laser(reduced damage)
            self.weaponType = random.randrange(1, 3)
            
            #Check for shooting
            if self.rect.y + (self.height / 2) >= 0:
                self.shootChance = random.randrange(1, 151)
            
            #Check for kamikaze strike
            if self.rect.y >= 0 and self.kamikaze == 0:
                self.kamikazeChance = random.randrange(1, 201)
                if self.kamikazeChance == 1:
                    self.kamikaze = 1
            # Check if dead
            if self.health <= 0 or self.rect.y > self.display_height:
                self.kill()
                
                
        def spawnDrop(self):
            k = random.randrange(1, 101)
            if k <= self.dropChance:
                return 1
            else:
                return 0

    #Class of alien boss bat (first boss, hard - ulra hard -> stats on final stage x4)        
    class AlienBossBat(Aliens):
        def __init__(self, dw, dh, w, h):
            super().__init__(dw, dh, w, h)
            
            self.image = bossBatImg
            self.x = (self.display_width / 2) - (self.width / 2)
            self.y = -self.height
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.image.set_colorkey(BLACK)
            self.weaponType = 0
            self.damage = 500
            self.health = 20000
            self.stamina = 20000
            self.speedx = 3
            self.speedy = 3
            self.rotationx = self.setRotationX()
            self.rotationy = 1
            self.dive = 0
            self.finalStage = 0
            self.shootChance = 0
            self.screenEnter = 0
            self.dropChance = 101
            self.slowed = 0
            self.slowDuration = 0.0
            self.slowflag = 0
            self.dissablesTimer = 1.0
        
        #Set side rotation
        def setRotationX(self):
            x = random.randrange(-1, 2)
            if x == 0:
                x = -1
            return x
        
        # Boss moves both directions
        def update(self):
            # Side steps logic
            if self.rotationx == 1 and self.rect.x <= 0:
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == 1 and self.rect.x + self.width < self.display_width and self.rect.x > 0:
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == 1 and self.rect.x + self.width >= self.display_width:
                self.rotationx = -1
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == -1 and self.rect.x > 0:
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == -1 and self.rect.x <= 0:
                self.rotationx = 1
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == -1 and self.rect.x >= self.display_width:
                self.rect.x += (self.speedx * self.rotationx)
            elif self.rotationx == -1 and self.rect.x < self.display_width:
                self.rect.x += (self.speedx * self.rotationx)
            
            # Forward steps
            if self.screenEnter == 0:
                if self.rect.y < 0:
                    self.rect.y += self.speedy
                    if self.rect.y >= 0:
                        self.screenEnter = 1
            else:
                if self.rect.y >= 0 and self.dive == 0:            
                    self.diveChance = random.randrange(1, 101)
                    if self.diveChance <= 3:
                        self.dive = 1          
                if self.dive == 1 and self.rotationy == 1:
                    self.rect.y += (self.rotationy * self.speedy)
                    if self.rect.y + self.height > (self.display_height / 2):
                        self.rotationy = -1
                        self.rect.y += (self.rotationy * self.speedy)
                elif self.dive == 1 and self.rotationy == -1:
                    self.rect.y += (self.rotationy * self.speedy)
                    if self.rect.y <= 0:
                        self.rotationy = 1
                        self.dive = 0
                        
            #Check if speed slowed down by frost laser and calculate time
            if self.slowed == 1:
                self.speedx = 1
                self.speedy = 1
                if time.time() - self.slowDuration > 0.0 and self.slowflag == 0:
                    self.slowDuration = time.time()
                    self.slowflag = 1
                elif self.slowflag == 1:
                    if time.time() - self.slowDuration > self.dissablesTimer:
                        self.slowed = 0
                        self.speedx = 3
                        self.speedy = 3
                        self.slowflag = 0
            
            #Check the weapon's type
            self.weaponType = random.randrange(1, 3)
            
            #Check for shooting chance
            if self.screenEnter == 1 :
                self.shootChance = random.randrange(1, 34)
                
            #Check if it's final stage and reset the stats
            if self.finalStage == 1:
                self.stamina = (4 * self.stamina)
                self.health = self.stamina
                
            #Check if died
            if self.health <= 0:
                self.kill()
                
        def spawnDrop(self):
            k = random.randrange(1, 101)
            if k <= self.dropChance:
                return 1
            else:
                return 0

    #Class of alien General (second boss(boss bat stats x2), hard - ultra hard -> stats on final stage x5)
    class AlienBossGeneral(Aliens):
        def __init__(self, dw, dh, w, h):
            super().__init__(dw, dh, w, h)
            
            self.image = bossGeneralImg
            self.x = (self.display_width / 2) - (self.width / 2)
            self.y = -self.height
            self.rect = self.image.get_rect(center = (self.x, self.y))
            self.image.set_colorkey(WHITE)
            self.weaponType = 0
            self.damage = 500
            self.health = 30000
            self.stamina = 30000
            self.speedx = 3
            self.speedy = 3
            self.rotationx = self.setRotationX()
            self.rotationy = 1
            self.dive = 0
            self.finaStage = 0
            self.screenEnter = 0
            self.shootChance = 0
            self.dropChance = 101
            self.slowed = 0
            self.slowDuration = 0.0
            self.slowflag = 0
            self.dissablesTimer = 1.0
        
        #Set side rotation
        def setRotationX(self):
            x = random.randrange(-1, 2)
            if x == 0:
                x = -1
            return x
        
        # Boss moves both directions
        def update(self):
            # Side steps logic
            if self.rotationx == 1 and self.rect.x <= 0:
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == 1 and self.rect.x + self.width < self.display_width and self.rect.x > 0:
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == 1 and self.rect.x + self.width >= self.display_width:
                self.rotationx = -1
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == -1 and self.rect.x > 0:
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == -1 and self.rect.x <= 0:
                self.rotationx = 1
                self.rect.x += (self.rotationx * self.speedx)
            elif self.rotationx == -1 and self.rect.x >= self.display_width:
                self.rect.x += (self.speedx * self.rotationx)
            elif self.rotationx == -1 and self.rect.x < self.display_width:
                self.rect.x += (self.speedx * self.rotationx)
            
            # Forward steps
            if self.screenEnter == 0:
                if self.rect.y < 0:
                    self.rect.y += self.speedy
                    if self.rect.y >= 0:
                        self.screenEnter = 1
            else:
                if self.rect.y >= 0 and self.dive == 0:            
                    self.diveChance = random.randrange(1, 101)
                    if self.diveChance <= 5:
                        self.dive = 1          
                if self.dive == 1 and self.rotationy == 1:
                    self.rect.y += (self.rotationy * self.speedy)
                    if self.rect.y + self.height > (self.display_height / 2):
                        self.rotationy = -1
                        self.rect.y += (self.rotationy * self.speedy)
                elif self.dive == 1 and self.rotationy == -1:
                    self.rect.y += (self.rotationy * self.speedy)
                    if self.rect.y <= 0:
                        self.rotationy = 1
                        self.dive = 0
                        
            #Check if speed slowed down by frost laser and calculate time
            if self.slowed == 1:
                self.speedx = 1
                self.speedy = 1
                if time.time() - self.slowDuration > 0.0 and self.slowflag == 0:
                    self.slowDuration = time.time()
                    self.slowflag = 1
                elif self.slowflag == 1:
                    if time.time() - self.slowDuration > self.dissablesTimer:
                        self.slowed = 0
                        self.speedx = 3
                        self.speedy = 3
                        self.slowflag = 0
            
            #Check the weapon's type
            self.weaponType = random.randrange(1, 3)
            
            #Check for shooting chance
            if self.screenEnter == 1 :
                self.shootChance = random.randrange(1, 34)
                
            #Check if it's the final stage and reset stats
            if self.finaStage == 1:
                self.stamina = (5 * self.stamina)
                self.health = self.stamina
                
            #Check if died
            if self.health <= 0:
                self.kill()
                
        def spawnDrop(self):
            k = random.randrange(1, 101)
            if k <= self.dropChance:
                return 1
            else:
                return 0
            
    class Missiles(pygame.sprite.Sprite):
        def __init__(self, dw, dh, x, y, wpn, pwlvl):
            super().__init__()
            
            self.weapon = wpn
            self.powerLevel = pwlvl
            self.posx = x
            self.posy = y
            self.setFire()
            self.rect = self.image.get_rect(center = (self.posx, self.posy))
            self.speedy = 8
            self.speedx = 0
            
        def setFire(self):
            if self.weapon == 1:
                self.image = bullets
            elif self.weapon == 2:
                if self.powerLevel == 1:
                    self.image = frostLaserL1
                elif self.powerLevel == 2:
                    self.image = frostLaserL2
                else:
                    self.image = frostLaserL3
            elif self.weapon == 3:
                if self.powerLevel == 1:
                    self.image = fireLaserL1
                elif self.powerLevel == 2:
                    self.image = fireLaserL2
                else:
                    self.image = fireLaserL3
                    
        def setMultiMissiles(self, x):
            if x == 2:
                self.image = leftBullets
                self.rect = self.image.get_rect(center = (self.posx, self.posy))
            elif x == 3:
                self.image = rightBullets
                self.rect = self.image.get_rect(center = (self.posx, self.posy))

        def update(self):
            self.rect.y -= self.speedy
            self.rect.x += self.speedx
            
    class AlienMissiles(pygame.sprite.Sprite):
        def __init__(self, dw, dh, x, y, t):
            super().__init__()
            
            self.weaponType = t
            self.setFire()
            self.rect = self.image.get_rect(center = (x, y))
            self.speedy = 8
        
        def setFire(self):
            if self.weaponType == 1:
                self.image = alien_FireLaser
            elif self.weaponType == 2:
                self.image = alien_FrostLaser
                    
        def update(self):
            self.rect.y += self.speedy
            
    #Drop - Power Up class
    class Drops(pygame.sprite.Sprite):
        def __init__(self, dw, dh, x, y):
            super().__init__()
            
            self.display_width = dw
            self.display_height = dh
            self.posx = x
            self.posy = y
            self.speedx = 2
            self.speedy = 2
            self.pickedUp = 0
            
        #Set Rotation
        def setRotation(self):
            self.rotationx = self.rotationy = random.randrange(-1, 5)
            if self.rotationx > 0:
                self.rotationx = self.rotationy = 1
            elif self.rotationx == 0:
                self.setRotation()
        
        #Set both side's rotation chance
        def setRotationChance(self):
            self.rotationxChance = random.randrange(1, 151)
            self.rotationyChance = random.randrange(1, 251)
            
        #Change rotation side
        def changeRotation(self):
            #Side steps rotation
            if self.rotationxChance == 1:
                if self.rotationx == 1:
                    self.rotationx = -1
                else:
                    self.rotationx = 1
            
            #Forward steps rotation
            if self.rotationyChance == 1:
                if self.rotationy == 1:
                    self.rotationy = -1
                else:
                    self.rotationy = 1
        
        #Movement           
        def move(self):
            self.rect.x += (self.rotationx * self.speedx)
            self.rect.y += (self.rotationy * self.speedy)
                    
        #Kill if picked up or went of the boundaries
        def checkStatus(self):
            if self.pickedUp == 1:
                self.kill()
            
            if self.rect.x > self.display_width or self.width < 0:
                self.kill()
            elif self.rect.y < 0 or self.rect.y > self.display_height:
                self.kill()
                
    #Hero status power ups
    class StaminaDrop(Drops):
        def __init__(self, dw, dh, x, y):
            super().__init__(dw, dh, x, y)
            
            self.type = 1
            self.image = staminaIcon
            self.rect = self.image.get_rect(center = (self.posx, self.posy))
            self.image.set_colorkey(YELLOW)
            self.width = 28
            self.height = 23
            
            self.setRotation()
            
        def update(self):
            #Movement
            self.move()       
            #Call both sides rotation chances
            self.setRotationChance()
            self.changeRotation()
            #Check drop status
            self.checkStatus()
            
    class HealDrop(Drops):
        def __init__(self, dw, dh, x, y):
            super().__init__(dw, dh, x, y)
            
            self.type = 2
            self.image = healIcon
            self.rect = self.image.get_rect(center = (self.posx, self.posy))
            self.image.set_colorkey(YELLOW)
            self.width = 28
            self.height = 23
            
            self.setRotation()
            
        def update(self):
            #Movement
            self.move()       
            #Call both sides rotation chances
            self.setRotationChance()
            self.changeRotation()
            #Check drop status
            self.checkStatus()
            
    class TenacityDrop(Drops):
        def __init__(self, dw, dh, x, y):
            super().__init__(dw, dh, x, y)
            
            self.type = 3
            self.image = tenacityIcon
            self.rect = self.image.get_rect(center = (self.posx, self.posy))
            self.image.set_colorkey(YELLOW)
            self.width = 28
            self.height = 23
            
            self.setRotation()
            
        def update(self):
            #Movement
            self.move()       
            #Call both sides rotation chances
            self.setRotationChance()
            self.changeRotation()
            #Check drop status
            self.checkStatus()
            
    class NanoshellDrop(Drops):
        def __init__(self, dw, dh, x, y):
            super().__init__(dw, dh, x, y)
            
            self.type = 4
            self.image = nanoshellIcon
            self.rect = self.image.get_rect(center = (self.posx, self.posy))
            self.image.set_colorkey(YELLOW)
            self.width = 28
            self.height = 22
            
            self.setRotation()
            
        def update(self):
            #Movement
            self.move()       
            #Call both sides rotation chances
            self.setRotationChance()
            self.changeRotation()
            #Check drop status
            self.checkStatus()
            
    #Hero weapon drops and power ups        
    class BulletDrop(Drops):
        def __init__(self, dw, dh, x, y):
            super().__init__(dw, dh, x, y)
                
            self.type = 1
            self.image = bulletIcon
            self.rect = self.image.get_rect(center = (self.posx, self.posy))
            self.image.set_colorkey(YELLOW)
            self.width = 28
            self.height = 23
            
            self.setRotation()
                
        def update(self):       
            #Movement
            self.move()       
            #Call both sides rotation chances
            self.setRotationChance()
            self.changeRotation()
            #Check drop status
            self.checkStatus()
            
    class FrostLaserDrop(Drops):
        def __init__(self, dw, dh, x, y):
            super().__init__(dw, dh, x, y)
                
            self.type = 1
            self.image = frostLaserIcon
            self.rect = self.image.get_rect(center = (self.posx, self.posy))
            self.image.set_colorkey(YELLOW)
            self.width = 28
            self.height = 23
            
            self.setRotation()
                
        def update(self):       
            #Movement
            self.move()       
            #Call both sides rotation chances
            self.setRotationChance()
            self.changeRotation()
            #Check drop status
            self.checkStatus()
            
    class FireLaserDrop(Drops):
        def __init__(self, dw, dh, x, y):
            super().__init__(dw, dh, x, y)
                
            self.type = 1
            self.image = fireLaserIcon
            self.rect = self.image.get_rect(center = (self.posx, self.posy))
            self.image.set_colorkey(YELLOW)
            self.width = 28
            self.height = 23
            
            self.setRotation()
                
        def update(self):       
            #Movement
            self.move()       
            #Call both sides rotation chances
            self.setRotationChance()
            self.changeRotation()
            #Check drop status
            self.checkStatus()

    class Background(pygame.sprite.Sprite):
        def __init__(self, dw, dh, y):
            super().__init__()
            
            self.motion = 1
            self.display_width = dw
            self.display_height = dh
            self.image = backgGalaxy
            self.rect = self.image.get_rect(center = (display_width / 2, y / 2))
            self.speedy = 2 * self.motion
            self.boss = 0

        def update(self):
            self.rect.y += self.speedy

        def setImage(self,x):
            if x == 1:
                self.image = backgPlanets
            elif x == 2:
                self.image = backgRepublic
            elif x == 3:
                self.image = backgThunderStorm

        def set_motion(self,x):
            self.motion = x
            self.speedy = 2 * self.motion

    #Message on screen function
    def text_objects(text, font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()        

    def message_display(text):
        gameOverText = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf,TextRect = text_objects(text, gameOverText)
        #TextSurf = gameOverText.render(gameOverText, True, WHITE)
        #TextRect = TextSurf.get_rect()
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update() 
        time.sleep(3)
        
    def Game_Over():
        message_display('YOU LOST')

    def game_Won():
        message_display('VICTORY')
        
    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font('freesansbold.ttf', size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    # Start Screen
    def show_go_screen():
        gameDisplay.blit(backgCosmos, cosmos)
        draw_text(gameDisplay, "Star Guardian!", 64, display_width / 2, display_height / 4)
        draw_text(gameDisplay, "Arrow keys move, Space to fire, Escape to exit", 22,display_width / 2, display_height / 2)
        draw_text(gameDisplay, "Press a key to begin", 18, display_width / 2, display_height * 3 / 4)
        pygame.display.flip()
        waiting = True
        
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    else:
                        waiting = False

    #Init --> Lets play, create character and enter loop
    show_go_screen()

    def game_Loop():     
        #Initialize lists
        all_sprites_list = pygame.sprite.Group()
        #audio
        airborne = game_path + 'airborne.wav'
        deadlocked = game_path + 'deadlocked.wav'
        finalbattle = game_path + 'finalbattle.wav'
        
        #Background image list
        background_list = pygame.sprite.Group()

        #Hero's fire lists according to weapon type and powerlevel
        center_bullet_fire_list = pygame.sprite.Group()
        left_bullet_fire_list = pygame.sprite.Group()
        right_bullet_fire_list = pygame.sprite.Group()
        fireLaser_fire_list = pygame.sprite.Group()
        frostLaser_fire_list = pygame.sprite.Group()
        
        #Alien's lists
        alien_private_list = pygame.sprite.Group()
        alien_private_fire_list = pygame.sprite.Group()
        
        alien_sergeant_list = pygame.sprite.Group()
        alien_sergeant_fire_list = pygame.sprite.Group()
        
        alien_captain_list = pygame.sprite.Group()
        alien_captain_FireLaser_fire_list = pygame.sprite.Group()
        alien_captain_FrostLaser_fire_list = pygame.sprite.Group()
        
        alien_bossBat_list= pygame.sprite.Group()
        alien_bossBat_FireLaser_fire_list = pygame.sprite.Group()
        alien_bossBat_FrostLaser_fire_list = pygame.sprite.Group()
        
        alien_bossGeneral_list = pygame.sprite.Group()
        alien_bossGeneral_FireLaser_fire_list = pygame.sprite.Group()
        alien_bossGeneral_FrostLaser_fire_list = pygame.sprite.Group()
        
        #Hero's drop lists
        stamina_drop_list = pygame.sprite.Group()
        heal_drop_list = pygame.sprite.Group()
        tenacity_drop_list = pygame.sprite.Group()
        nanoshell_drop_list = pygame.sprite.Group()
        bullet_drop_list = pygame.sprite.Group()
        frostLaser_drop_list = pygame.sprite.Group()
        fireLaser_drop_list = pygame.sprite.Group()

        game_stage = 1

        #Backgroubd Image init
        #Parameters (resolution x, resolution y, position of image according to resolution y)
        backgImage = Background(display_width,display_height, 768,)
        background_list.add(backgImage)
        all_sprites_list.add(backgImage)
        backgImage = Background(display_width,display_height, -768,)
        background_list.add(backgImage)
        all_sprites_list.add(backgImage)
        bossbackgImage = Background(display_width,display_height, -768,)
        background_list.add(bossbackgImage)
        all_sprites_list.add(bossbackgImage)

        hero = Player(display_width,display_height, 80, 79)
        all_sprites_list.add(hero)
        
        #Flags for resets etc...
        stage_check = game_stage
        backg_motion = 0
        
        heroFired = 0
        heroSingleBulleti = 0
        heroDoubleBulleti = 0
        heroTripleBulleti =0
        heroFireLaseri = 0
        heroFrostLaseri = 0
        
        private_spawn_time_limit = 4.0
        private_spawn_time = 0.0
        privateFired = 0
        privatei = 0
        
        sergeant_spawn_time_limit = 8.0
        sergeant_spawn_time = 0.0
        sergeantFired = 0
        sergeanti = 0
        
        captain_spawn_time_limit = 10.0
        captain_spawn_time = 0.0
        captainFired = 0
        captaini = 0 
        
        bossBatFired = 0
        bossBati = 0
        bossBatdead = 1
        
        bossGeneralFired = 0
        bossGenerali = 0
        bossGeneraldead = 1

        boss_spawn = 0
        
        staminaDropi = 0
        healDropi = 0
        tenacityDropi = 0
        nanoshellDropi = 0
        bulletDropi = 0
        frostLaserDropi = 0
        fireLaserDropi = 0
        
        x = 0
        y = 0
        i = 0
        l = 0

        print_stage = 1
        print_stageflag = 0
        print_stageDuration = 3.0
        print_stageTime = 0
        
        music = 0
        victory = 0
        gameOver = False
        score = 0
        addFire = False
        
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x = -1
                        i = 1
                    elif event.key == pygame.K_RIGHT:
                        x = 1
                        i = 1
                    elif event.key == pygame.K_UP:
                        y = -1
                        i = 2
                    elif event.key == pygame.K_DOWN:
                        y = 1
                        i = 2
                    elif event.key == pygame.K_SPACE:
                        addFire = True
                    
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x = 0
                        i = 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y = 0
                        i = 2
                    elif event.key == pygame.K_SPACE:
                        addFire = False
                    elif event.key == pygame.K_ESCAPE:
                            game_Over = True
                            pygame.quit()
                            return

            
            if addFire:
                if score % 5 == 0:
                    if hero.weapon == 1:
                        if hero.powerLevel == 1:
                            centerbullet = Missiles(display_width,display_height, hero.rect.x + 35, hero.rect.y, hero.weapon, hero.powerLevel)
                            all_sprites_list.add(centerbullet)
                            center_bullet_fire_list.add(centerbullet)
                            heroSingleBulleti = 1
                        elif hero.powerLevel == 2:
                            leftbullet = Missiles(display_width,display_height,hero.rect.x + 29, hero.rect.y, hero.weapon, hero.powerLevel)
                            leftbullet.setMultiMissiles(2)
                            all_sprites_list.add(leftbullet)
                            left_bullet_fire_list.add(leftbullet)
                            leftbullet.speedx = -3
                                    
                            rightbullet = Missiles(display_width,display_height,hero.rect.x + 39, hero.rect.y, hero.weapon, hero.powerLevel)
                            rightbullet.setMultiMissiles(3)
                            all_sprites_list.add(rightbullet)
                            right_bullet_fire_list.add(rightbullet)
                            rightbullet.speedx = 3
                            heroDoubleBulleti = 1
                        else:
                            centerbullet = Missiles(display_width,display_height, hero.rect.x + 35, hero.rect.y, hero.weapon, hero.powerLevel)
                            all_sprites_list.add(centerbullet)
                            center_bullet_fire_list.add(centerbullet)
                                    
                            leftbullet = Missiles(display_width,display_height,hero.rect.x + 29, hero.rect.y, hero.weapon, hero.powerLevel)
                            leftbullet.setMultiMissiles(2)
                            all_sprites_list.add(leftbullet)
                            left_bullet_fire_list.add(leftbullet)
                            leftbullet.speedx = -2
                                    
                            rightbullet = Missiles(display_width,display_height,hero.rect.x + 39, hero.rect.y, hero.weapon, hero.powerLevel)
                            rightbullet.setMultiMissiles(3)
                            all_sprites_list.add(rightbullet)
                            right_bullet_fire_list.add(rightbullet)
                            rightbullet.speedx = 2
                            heroTripleBulleti = 1
                                
                    elif hero.weapon == 2:
                        if hero.powerLevel == 1:
                            frostLaser = Missiles(display_width, display_height,(hero.rect.x + ((hero.width / 2) - 7)), hero.rect.y - 5, hero.weapon, hero.powerLevel)
                            all_sprites_list.add(frostLaser)
                            frostLaser_fire_list.add(frostLaser)                         
                        elif hero.powerLevel == 2:
                            frostLaser = Missiles(display_width, display_height,(hero.rect.x + ((hero.width / 2) - 7)), hero.rect.y - 5, hero.weapon, hero.powerLevel)
                            all_sprites_list.add(frostLaser)
                            frostLaser_fire_list.add(frostLaser)
                        else: 
                            frostLaser = Missiles(display_width, display_height, (hero.rect.x + ((hero.width / 2) - 7)), hero.rect.y - 5, hero.weapon, hero.powerLevel)
                            all_sprites_list.add(frostLaser)
                            frostLaser_fire_list.add(frostLaser)
                        heroFrostLaseri = 1
                    elif hero.weapon == 3:
                        if hero.powerLevel == 1:
                            fireLaser = Missiles(display_width, display_height, (hero.rect.x +((hero.width / 2) - 7)), hero.rect.y - 5, hero.weapon, hero.powerLevel)
                            all_sprites_list.add(fireLaser)
                            fireLaser_fire_list.add(fireLaser)
                        elif hero.powerLevel == 2:
                            fireLaser = Missiles(display_width, display_height, (hero.rect.x +((hero.width / 2) - 7)), hero.rect.y - 5, hero.weapon, hero.powerLevel)
                            all_sprites_list.add(fireLaser)
                            fireLaser_fire_list.add(fireLaser)
                        else:
                            fireLaser = Missiles(display_width, display_height, (hero.rect.x +((hero.width / 2) - 7)), hero.rect.y - 5, hero.weapon, hero.powerLevel)
                            all_sprites_list.add(fireLaser)
                            fireLaser_fire_list.add(fireLaser)
                        heroFireLaseri = 1
                    heroFired = 1
                        
            #Move the spaceship with boundaries
            if i == 1:
                hero.moveX(x)
            elif i == 2:
                hero.moveY(y)
            
            if hero.rect.x > display_width - hero.width:
                hero.setPosx(display_width - hero.width)
            elif hero.rect.x < 0:
                hero.setPosx(0)
            elif hero.rect.y < 0:
                hero.setPosy(0)
            elif hero.rect.y > display_height - hero.height:
                hero.setPosy(display_height - hero.height)

            #gameDisplay.fill(BLACK)
            for backgImage in background_list:
                if backgImage.rect.y > display_height:
                    backgImage.rect.y = (-1) * display_height

           
            #Aliens spawn
            #1)Private alien spawns in every game stage
            if score >= 100:
                if bossBatdead == 1 and bossGeneraldead == 1:
                    if time.time() - private_spawn_time > private_spawn_time_limit:
                        for spawn in range(8):
                            private = AlienPrivate(display_width, display_height, 50, 88)
                            all_sprites_list.add(private)
                            alien_private_list.add(private)
                            
                            if game_stage == 2:
                                private.damage = private.damage * 2
                                private.health = private.health * 2
                            elif game_stage == 3:
                                private.damage = private.damage * 3
                                private.health = private.health * 3
                        if private_spawn_time_limit < 8:
                            private_spawn_time_limit += 1.0
                        private_spawn_time = time.time()
                        privatei = 1
            #2)Sergreant spawns at stage 2 and 3
            if game_stage == 2:
                if bossBatdead == 1 and bossGeneraldead == 1:
                    if time.time() - sergeant_spawn_time > sergeant_spawn_time_limit:
                        for spawn_sergeant in range(3):
                            sergeant = AlienSergeant(display_width, display_height, 50, 88)
                            all_sprites_list.add(sergeant)
                            alien_sergeant_list.add(sergeant)
                        sergeant_spawn_time = time.time()
                        sergeanti = 1
            elif game_stage == 3:
                if bossBatdead == 1 and bossGeneraldead == 1:
                    if time.time() - sergeant_spawn_time > sergeant_spawn_time_limit:
                        for spawn_sergeant in range(6):
                            sergeant = AlienSergeant(display_width, display_height, 50, 88)
                            all_sprites_list.add(sergeant)
                            alien_sergeant_list.add(sergeant)
                            sergeant.damage = sergeant.damage * 2    
                            sergeant.health = sergeant.health * 2
                        sergeant_spawn_time = time.time()
                        sergeanti = 1
                    
            #3)Captain spawn at stage 2(less numbers) and 3(greater numbers)
            if game_stage == 2:
                if bossBatdead == 1 and bossGeneraldead == 1:
                    if time.time() - captain_spawn_time > captain_spawn_time_limit:
                        for spawn_captain in range(2):
                            captain = AlienCaptain(display_width, display_height, 50, 95)
                            all_sprites_list.add(captain)
                            alien_captain_list.add(captain)
                        captain_spawn_time = time.time()
                        captaini = 1
            elif game_stage == 3:
                if bossBatdead == 1 and bossGeneraldead == 1:
                    if time.time() - captain_spawn_time > captain_spawn_time_limit:
                        for spawn_captain in range(4):
                            captain = AlienCaptain(display_width, display_height, 50, 95)
                            all_sprites_list.add(captain)
                            alien_captain_list.add(captain)
                            captain.damage = captain.damage * 2
                            captain.health = captain.health * 2
                        captain_spawn_time = time.time()
                        captaini = 1
                    
            #4)Boss Bat spawns at stage 1 and 3(increased stats)
            if game_stage == 1 and score >= 10000 and bossBatdead == 1:
                bossBat = AlienBossBat(display_width, display_height, 80, 35)
                all_sprites_list.add(bossBat)
                alien_bossBat_list.add(bossBat)
                bossBati = 1
                bossBatdead = 0

            elif game_stage == 3 and score >= 60100 and bossBatdead == 1:
                bossBat = AlienBossBat(display_width, display_height, 80, 35)
                all_sprites_list.add(bossBat)
                alien_bossBat_list.add(bossBat)
                bossBat.health = bossBat.health * 4
                bossBat.stamina = bossBat.stamina *4
                bossBati = 1
                bossBatdead = 0
                
            #5)Boss General of the army spawns at stage 2 and 3(increased stats)
            if game_stage == 2 and score >= 30000 and bossGeneraldead == 1:
                bossGeneral = AlienBossGeneral(display_width, display_height, 120, 119)
                all_sprites_list.add(bossGeneral)
                alien_bossGeneral_list.add(bossGeneral)
                bossGenerali = 1
                bossGeneraldead = 0
                backg_motion = 0

            elif game_stage == 3 and score >= 60100 and bossGeneraldead == 1:
                bossGeneral = AlienBossGeneral(display_width, display_height, 120, 119)
                all_sprites_list.add(bossGeneral)
                alien_bossGeneral_list.add(bossGeneral)
                bossGeneral.health = bossGeneral.health * 5
                bossGeneral.stamina = bossGeneral.stamina * 5
                bossGenerali = 1
                bossGeneraldead = 0
                backg_motion = 0
            
            #Alien's missiles spawn
            #1)Private's missiles
            if privatei == 1:
                for private in alien_private_list:
                    if private.shootChance == 1:
                        alFireLaser = AlienMissiles(display_width, display_height, (private.rect.x + (private.width / 2)) - 7, private.rect.y + private.height, 1)
                        all_sprites_list.add(alFireLaser)
                        alien_private_fire_list.add(alFireLaser)
                        privateFired = 1
            
            #2)Sergeant's missiles
            if sergeanti == 1:
                for sergeant in alien_sergeant_list:
                    if sergeant.shootChance == 1:
                        alFrostLaser = AlienMissiles(display_width, display_height, (sergeant.rect.x + (sergeant.width / 2) - 3), sergeant.rect.y + sergeant.height, 2)
                        all_sprites_list.add(alFrostLaser)
                        alien_sergeant_fire_list.add(alFrostLaser)
                        sergeantFired = 1
                        
            #3)Captain's missiles
            if captaini == 1:
                for captain in alien_captain_list:
                    if captain.shootChance == 1:
                        if captain.weaponType == 1:
                            alFireLaser = AlienMissiles(display_width, display_height, (captain.rect.x + (captain.width / 2)), captain.rect.y + captain.height, 1)
                            all_sprites_list.add(alFireLaser)
                            alien_captain_FireLaser_fire_list.add(alFireLaser)
                            captainFired = 1
                        elif captain.weaponType == 2:
                            alFrostLaser = AlienMissiles(display_width, display_height, (captain.rect.x + (captain.width / 2)), captain.rect.y + captain.height, 2)
                            all_sprites_list.add(alFrostLaser)
                            alien_captain_FrostLaser_fire_list.add(alFrostLaser)
                            captainFired = 1
                            
            #4)Boss Bat's missiles
            if bossBati == 1:
                for bossBat in alien_bossBat_list:
                    if bossBat.shootChance == 1:
                        if bossBat.weaponType == 1:
                            #Left Cannon
                            alFireLaser = AlienMissiles(display_width, display_height, (bossBat.rect.x - 3), (bossBat.rect.y + 47), 1)
                            all_sprites_list.add(alFireLaser)
                            alien_bossBat_FireLaser_fire_list.add(alFireLaser)
                        
                            #Right cannon
                            alFrostLaser = AlienMissiles(display_width, display_height, (bossBat.rect.x + (bossBat.width - 12)), (bossBat.rect.y + 47), 2)
                            all_sprites_list.add(alFrostLaser)
                            alien_bossBat_FrostLaser_fire_list.add(alFrostLaser)
                            bossBatFired = 1
                        else:
                            #Left Cannon
                            alFrostLaser = AlienMissiles(display_width, display_height, (bossBat.rect.x - 3), (bossBat.rect.y + 47), 2)
                            all_sprites_list.add(alFrostLaser)
                            alien_bossBat_FrostLaser_fire_list.add(alFrostLaser)
                        
                            #Right Cannon
                            alFireLaser = AlienMissiles(display_width, display_height, (bossBat.rect.x + (bossBat.width - 12)), (bossBat.rect.y + 47), 1)
                            all_sprites_list.add(alFireLaser)
                            alien_bossBat_FireLaser_fire_list.add(alFireLaser)
                            bossBatFired = 1
                            
            #5)Boss General's missiles
            if bossGenerali == 1:
                for bossGeneral in alien_bossGeneral_list:
                    if bossGeneral.shootChance == 1:
                        if bossGeneral.weaponType == 1:
                            #Left Cannon
                            alFireLaser = AlienMissiles(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 51), 1)
                            all_sprites_list.add(alFireLaser)
                            alien_bossGeneral_FireLaser_fire_list.add(alFireLaser)
                        
                            #Right cannon
                            alFrostLaser = AlienMissiles(display_width, display_height, (bossGeneral.rect.x + 86), (bossGeneral.rect.y + 51), 2)
                            all_sprites_list.add(alFrostLaser)
                            alien_bossGeneral_FrostLaser_fire_list.add(alFrostLaser)
                            bossGeneralFired = 1
                        else:
                            #Left Cannon
                            alFrostLaser = AlienMissiles(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 51), 2)
                            all_sprites_list.add(alFrostLaser)
                            alien_bossGeneral_FrostLaser_fire_list.add(alFrostLaser)
                        
                            #Right Cannon
                            alFireLaser = AlienMissiles(display_width, display_height, (bossGeneral.rect.x + 86), (bossGeneral.rect.y + 51), 1)
                            all_sprites_list.add(alFireLaser)
                            alien_bossGeneral_FireLaser_fire_list.add(alFireLaser)
                            bossGeneralFired = 1
                        
            #Aliens and hero collision check
            #1)Private - hero collision
            if privatei == 1:
                private_hero_collision_list = pygame.sprite.spritecollide(hero, alien_private_list, False)
                if private_hero_collision_list:
                    hero.health = 0
                    
            #2)Sergeant - hero collision
            if sergeanti == 1:
                sergeant_hero_collision_list = pygame.sprite.spritecollide(hero, alien_sergeant_list, False)
                if sergeant_hero_collision_list:
                    hero.health = 0
                    
            #3)Captain - hero collision
            if captaini == 1:
                captain_hero_collision_list = pygame.sprite.spritecollide(hero, alien_captain_list, False)
                if captain_hero_collision_list:
                    hero.health = 0
                    
            #4)Boss Bat - hero collision
            if bossBati == 1:
                bossBat_hero_collision_list = pygame.sprite.spritecollide(hero, alien_bossBat_list, False)
                if bossBat_hero_collision_list:
                    hero.health = 0
                    
            #5)Boss General - gero collision
            if bossGenerali == 1:
                bossGeneral_hero_collision_list = pygame.sprite.spritecollide(hero, alien_bossGeneral_list, False)
                if bossGeneral_hero_collision_list:
                    hero.health = 0
                
            #Check the hero's missile status
            if heroFired == 1:  
                
                #1)For weapon type 1, Bullets
                if heroSingleBulleti == 1:
                    for centerbullet in center_bullet_fire_list: 
                        
                        #1)Hero - private alien missile collision
                        alien_private_hit_list = pygame.sprite.spritecollide(centerbullet, alien_private_list, False)
                        for private in alien_private_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            private.health = (private.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if private.health <= 0:
                                score += 100
                                if private.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #2)Hero - sergeant alien missile collision
                        alien_sergeant_hit_list = pygame.sprite.spritecollide(centerbullet, alien_sergeant_list, False)
                        for sergeant in alien_sergeant_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            sergeant.health = (sergeant.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if sergeant.health <= 0:
                                score += 200
                                if sergeant.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #3)Hero - captain alien missile collision
                        alien_captain_hit_list = pygame.sprite.spritecollide(centerbullet, alien_captain_list, False)
                        for captain in alien_captain_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            captain.health = (captain.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if captain.health <= 0:
                                score += 500
                                if captain.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #4)Hero - boss Bat alien missile collision
                        alien_bossBat_hit_list = pygame.sprite.spritecollide(centerbullet, alien_bossBat_list, False)
                        if alien_bossBat_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            bossBat.health = (bossBat.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if bossBat.health <= 0:
                                score += 1000
                                if bossBat.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                                                
                                victory += 1
                                bossBati = 0
                                all_sprites_list.remove(bossBat)
                                alien_bossBat_list.remove(bossBat)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossBatdead = 1
                                
                        #5)hero - boss General alien missile collision
                        alien_bossGeneral_hit_list = pygame.sprite.spritecollide(centerbullet, alien_bossGeneral_list, False)
                        if alien_bossGeneral_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            bossGeneral.health = (bossGeneral.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if bossGeneral.health <= 0:
                                score += 1500
                                if bossGeneral.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                                            
                                victory += 1
                                bossGenerali = 0
                                all_sprites_list.remove(bossGeneral)
                                alien_bossGeneral_list.remove(bossGeneral)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossGeneraldead = 1
                        
                        # Remove hero's missile if goes off the boundaries
                        if centerbullet.rect.y < -centerbullet.rect.y:
                            center_bullet_fire_list.remove(centerbullet)
                            all_sprites_list.remove(centerbullet)
                            centerbullet.remove()
                
                #Check for double bullets
                if heroDoubleBulleti == 1:  
                    
                    #Left Bullet
                    for leftbullet in left_bullet_fire_list:                 
                        #1)Hero - private alien missile collision
                        alien_private_left_hit_list = pygame.sprite.spritecollide(leftbullet, alien_private_list, False)
                        for private in alien_private_left_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            private.health = (private.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if private.health <= 0:
                                score += 100
                                if private.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #2)Hero - sergeant alien missile collision
                        alien_sergeant_hit_list = pygame.sprite.spritecollide(leftbullet, alien_sergeant_list, False)
                        for sergeant in alien_sergeant_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            sergeant.health = (sergeant.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if sergeant.health <= 0:
                                score += 200
                                if sergeant.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #3)Hero - captain alien missile colision
                        alien_captain_hit_list = pygame.sprite.spritecollide(leftbullet, alien_captain_list, False)
                        for captain in alien_captain_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            captain.health = (captain.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if captain.health <= 0:
                                score += 500
                                if captain.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #4)Hero - Boss Bat alien missile colision
                        alien_bossBat_hit_list = pygame.sprite.spritecollide(leftbullet, alien_bossBat_list, False)
                        for bossBat in alien_bossBat_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            bossBat.health = (bossBat.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if bossBat.health <= 0:
                                score += 1000
                                if bossBat.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                    
                                victory += 1
                                bossBati = 0
                                all_sprites_list.remove(bossBat)
                                alien_bossBat_list.remove(bossBat)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossBatdead = 1
                                    
                                        
                        #5)Hero - Boss General missile collision
                        alien_bossGeneral_hit_list = pygame.sprite.spritecollide(leftbullet, alien_bossGeneral_list, False)
                        for bossGeneral in alien_bossGeneral_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            bossGeneral.health = (bossGeneral.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if bossGeneral.health <= 0:
                                score += 1500
                                if bossGeneral.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                
                                victory += 1
                                bossGenerali = 0
                                all_sprites_list.remove(bossGeneral)
                                alien_bossGeneral_list.remove(bossGeneral)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossGeneraldead = 1
                                        
                        # Remove hero's missile if goes off the boundaries
                        if leftbullet.rect.y < -leftbullet.rect.y:
                            left_bullet_fire_list.remove(leftbullet)
                            all_sprites_list.remove(leftbullet)
                            leftbullet.remove()
                                        
                    #Right Bullet
                    for rightbullet in right_bullet_fire_list:                 
                        #1)Hero - private alien missile collision
                        alien_private_right_hit_list = pygame.sprite.spritecollide(rightbullet, alien_private_list, False)
                        for private in alien_private_right_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            private.health = (private.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if private.health <= 0:
                                score += 100
                                if private.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #2)Hero - sergeant missile collision              
                        alien_sergeant_hit_list = pygame.sprite.spritecollide(rightbullet, alien_sergeant_list, False)
                        for sergeant in alien_sergeant_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            sergeant.health = (sergeant.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if sergeant.health <= 0:
                                score += 200
                                if sergeant.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #3)Hero - Captain missile collision
                        alien_captain_hit_list = pygame.sprite.spritecollide(rightbullet, alien_captain_list, False)
                        for captain in alien_captain_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            captain.health = (captain.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if captain.health <= 0:
                                score += 500
                                if captain.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                    
                        #4)Hero - Boss Bat missile collision
                        alien_bossBat_hit_list = pygame.sprite.spritecollide(rightbullet, alien_bossBat_list, False)
                        for bossBat in alien_bossBat_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            bossBat.health = (bossBat.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if bossBat.health <= 0:
                                score += 1000
                                if bossBat.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1

                                victory += 1
                                bossBati = 0
                                all_sprites_list.remove(bossBat)
                                alien_bossBat_list.remove(bossBat)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossBatdead = 1
                                        
                        #5)Hero - Boss General missile collision
                        alien_bossGeneral_hit_list = pygame.sprite.spritecollide(rightbullet, alien_bossBat_list, False)
                        for bossGeneral in alien_bossGeneral_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            bossGeneral.health = (bossGeneral.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if bossGeneral.health <= 0:
                                score += 1500
                                if bossGeneral.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                                            
                                victory += 1
                                bossGenerali = 0
                                all_sprites_list.remove(bossGeneral)
                                alien_bossGeneral_list.remove(bossGeneral)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossGeneraldead = 1
                                    
                                            
                        # Remove hero's missile if goes off the boundaries
                        if rightbullet.rect.y < -rightbullet.rect.y:
                            right_bullet_fire_list.remove(rightbullet)
                            all_sprites_list.remove(rightbullet)
                            rightbullet.remove()
                                        
                #2)Check for triple bullets
                if heroTripleBulleti == 1:
                    
                    #Center bullet
                    for centerbullet in center_bullet_fire_list:                 
                        #1)Hero - private alien missile collision
                        alien_private_hit_list = pygame.sprite.spritecollide(centerbullet, alien_private_list, False)
                        for private in alien_private_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            private.health = (private.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if private.health <= 0:
                                score += 100
                                if private.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #2)Hero - sergeant alien missile collision
                        alien_sergeant_hit_list = pygame.sprite.spritecollide(centerbullet, alien_sergeant_list, False)
                        for sergeant in alien_sergeant_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            sergeant.health = (sergeant.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if sergeant.health <= 0:
                                score += 200
                                if sergeant.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #3)Hero - captain alien missile collision
                        alien_captain_hit_list = pygame.sprite.spritecollide(centerbullet, alien_captain_list, False)
                        for captain in alien_captain_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            captain.health = (captain.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if captain.health <= 0:
                                score += 500
                                if captain.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #4)Hero - boss Bat alien missile collision
                        alien_bossBat_hit_list = pygame.sprite.spritecollide(centerbullet, alien_bossBat_list, False)
                        if alien_bossBat_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            bossBat.health = (bossBat.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if bossBat.health <= 0:
                                score += 1000
                                if bossBat.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1

                                victory += 1
                                bossBati = 0
                                all_sprites_list.remove(bossBat)
                                alien_bossBat_list.remove(bossBat)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossBatdead = 1
                                
                        #5)hero - boss General alien missile collision
                        alien_bossGeneral_hit_list = pygame.sprite.spritecollide(centerbullet, alien_bossGeneral_list, False)
                        if alien_bossGeneral_hit_list:
                            center_bullet_fire_list.remove(centerbullet)
                            bossGeneral.health = (bossGeneral.health - hero.damage)
                            all_sprites_list.remove(centerbullet)
                            if bossGeneral.health <= 0:
                                score += 1500
                                if bossGeneral.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                
                                victory += 1
                                bossGenerali = 0
                                all_sprites_list.remove(bossGeneral)
                                alien_bossGeneral_list.remove(bossGeneral)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossGeneraldead = 1
                        
                        # Remove hero's missile if goes off the boundaries
                        if centerbullet.rect.y < -centerbullet.rect.y:
                            center_bullet_fire_list.remove(centerbullet)
                            all_sprites_list.remove(centerbullet)
                            centerbullet.remove()
                            
                    #Left Bullet
                    for leftbullet in left_bullet_fire_list:                 
                        #1)Hero - private alien missile collision
                        alien_private_left_hit_list = pygame.sprite.spritecollide(leftbullet, alien_private_list, False)
                        for private in alien_private_left_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            private.health = (private.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if private.health <= 0:
                                score += 100
                                if private.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #2)Hero - sergeant alien missile collision
                        alien_sergeant_hit_list = pygame.sprite.spritecollide(leftbullet, alien_sergeant_list, False)
                        for sergeant in alien_sergeant_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            sergeant.health = (sergeant.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if sergeant.health <= 0:
                                score += 200
                                if sergeant.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #3)Hero - captain alien missile colision
                        alien_captain_hit_list = pygame.sprite.spritecollide(leftbullet, alien_captain_list, False)
                        for captain in alien_captain_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            captain.health = (captain.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if captain.health <= 0:
                                score += 500
                                if captain.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #4)Hero - Boss Bat alien missile colision
                        alien_bossBat_hit_list = pygame.sprite.spritecollide(leftbullet, alien_bossBat_list, False)
                        for bossBat in alien_bossBat_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            bossBat.health = (bossBat.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if bossBat.health <= 0:
                                score += 1000
                                if bossBat.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                    
                                victory += 1
                                bossBati = 0
                                all_sprites_list.remove(bossBat)
                                alien_bossBat_list.remove(bossBat)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossBatdead = 1
                                        
                        #5)Hero - Boss general missile collision
                        alien_bossGeneral_hit_list = pygame.sprite.spritecollide(leftbullet, alien_bossGeneral_list, False)
                        for bossGeneral in alien_bossGeneral_hit_list:
                            left_bullet_fire_list.remove(leftbullet)
                            bossGeneral.health = (bossGeneral.health - hero.damage)
                            all_sprites_list.remove(leftbullet)
                            if bossGeneral.health <= 0:
                                score += 1500
                                if bossGeneral.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                                victory += 1
                                bossGenerali = 0
                                all_sprites_list.remove(bossGeneral)
                                alien_bossGeneral_list.remove(bossGeneral)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossGeneraldead = 1
                        
                        # Remove hero's missile if goes off the boundaries
                        if leftbullet.rect.y < -leftbullet.rect.y:
                            left_bullet_fire_list.remove(leftbullet)
                            all_sprites_list.remove(leftbullet)
                            leftbullet.remove()
                            
                    #Right Bullet
                    for rightbullet in right_bullet_fire_list:                 
                        #1)Hero - private alien missile collision
                        alien_private_right_hit_list = pygame.sprite.spritecollide(rightbullet, alien_private_list, False)
                        for private in alien_private_right_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            private.health = (private.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if private.health <= 0:
                                score += 100
                                if private.spawnDrop():
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #2)Hero - sergeant missile collision              
                        alien_sergeant_hit_list = pygame.sprite.spritecollide(rightbullet, alien_sergeant_list, False)
                        for sergeant in alien_sergeant_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            sergeant.health = (sergeant.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if sergeant.health <= 0:
                                score += 200
                                if sergeant.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #3)Hero - Captain missile collision
                        alien_captain_hit_list = pygame.sprite.spritecollide(rightbullet, alien_captain_list, False)
                        for captain in alien_captain_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            captain.health = (captain.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if captain.health <= 0:
                                score += 500
                                if captain.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                        #4)Hero - Boss Bat missile collision
                        alien_bossBat_hit_list = pygame.sprite.spritecollide(rightbullet, alien_bossBat_list, False)
                        for bossBat in alien_bossBat_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            bossBat.health = (bossBat.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if bossBat.health <= 0:
                                score += 1000
                                if bossBat.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1

                                victory += 1
                                bossBati = 0
                                all_sprites_list.remove(bossBat)
                                alien_bossBat_list.remove(bossBat)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossBatdead = 1
                                        
                        #5)Hero - Boss General missile collision
                        alien_bossGeneral_hit_list = pygame.sprite.spritecollide(rightbullet, alien_bossGeneral_list, False)
                        for bossGeneral in alien_bossGeneral_hit_list:
                            right_bullet_fire_list.remove(rightbullet)
                            bossGeneral.health = (bossGeneral.health - hero.damage)
                            all_sprites_list.remove(rightbullet)
                            if bossGeneral.health <= 0:
                                score += 1500
                                if bossGeneral.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                        
                                victory += 1
                                bossGenerali = 0
                                all_sprites_list.remove(bossGeneral)
                                alien_bossGeneral_list.remove(bossGeneral)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossGeneraldead = 1
                                            
                        # Remove hero's missile if goes off the boundaries
                        if rightbullet.rect.y < -rightbullet.rect.y:
                            right_bullet_fire_list.remove(rightbullet)
                            all_sprites_list.remove(rightbullet)
                            rightbullet.remove()
                            
                            
                #2)For weapon type 2, Frost Laser
                if heroFrostLaseri == 1:
                    for frostLaser in frostLaser_fire_list:                 
                        #1)Hero - private alien missile collision
                        alien_private_frost_hit_list = pygame.sprite.spritecollide(frostLaser, alien_private_list, False)
                        for private in alien_private_frost_hit_list:
                            frostLaser_fire_list.remove(frostLaser)
                            private.health = (private.health - hero.damage)
                            private.slowed = 1
                            private.slowflag = 0
                            all_sprites_list.remove(frostLaser)
                            if private.health <= 0:
                                score += 100
                                if private.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #2)Hero - sergeant alien missile collision
                        alien_sergeant_frost_hit_list = pygame.sprite.spritecollide(frostLaser, alien_sergeant_list, False)
                        for sergeant in alien_sergeant_frost_hit_list:
                            frostLaser_fire_list.remove(frostLaser)
                            sergeant.health = (sergeant.health - hero.damage)
                            sergeant.slowed = 1
                            sergeant.slowflag = 0
                            all_sprites_list.remove(frostLaser)
                            if sergeant.health <= 0:
                                score += 200
                                if sergeant.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #3)Hero - captain alien missile collision
                        alien_captain_frost_hit_list = pygame.sprite.spritecollide(frostLaser, alien_captain_list, False)
                        for captain in alien_captain_frost_hit_list:
                            frostLaser_fire_list.remove(frostLaser)
                            captain.health = (captain.health - hero.damage)
                            captain.slowed = 1
                            captain.slowflag = 0
                            all_sprites_list.remove(frostLaser)
                            if captain.health <= 0:
                                score += 500
                                if captain.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #4)Hero - boss Bat alien missile collision
                        alien_bossBat_frost_hit_list = pygame.sprite.spritecollide(frostLaser, alien_bossBat_list, False)
                        if alien_bossBat_frost_hit_list:
                            frostLaser_fire_list.remove(frostLaser)
                            bossBat.health = (bossBat.health - hero.damage)
                            bossBat.slowed = 1
                            bossBat.slowflag = 0
                            all_sprites_list.remove(frostLaser)
                            if bossBat.health <= 0:
                                score += 1000
                                if bossBat.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                    
                                victory += 1
                                bossBati = 0
                                all_sprites_list.remove(bossBat)
                                alien_bossBat_list.remove(bossBat)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossBatdead = 1
                                
                        #5)hero - boss General alien missile collision
                        alien_bossGeneral_frost_hit_list = pygame.sprite.spritecollide(frostLaser, alien_bossGeneral_list, False)
                        if alien_bossGeneral_frost_hit_list:
                            frostLaser_fire_list.remove(frostLaser)
                            bossGeneral.health = (bossGeneral.health - hero.damage)
                            bossGeneral.slowed = 1
                            bossGeneral.slowflag = 0
                            all_sprites_list.remove(frostLaser)
                            if bossGeneral.health <= 0:
                                score += 1500
                                if bossGeneral.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                
                                victory += 1
                                bossGenerali = 0
                                all_sprites_list.remove(bossGeneral)
                                alien_bossGeneral_list.remove(bossGeneral)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                bossGeneraldead = 1
                        
                        # Remove hero's missile if goes off the boundaries
                        if frostLaser.rect.y < -frostLaser.rect.y:
                            frostLaser_fire_list.remove(frostLaser)
                            all_sprites_list.remove(frostLaser)
                            frostLaser.remove()
                
                #3)Check for weapon type 3, FireLaser
                if heroFireLaseri == 1:
                    for fireLaser in fireLaser_fire_list:                 
                        #1)Hero - private alien missile collision
                        alien_private_fire_hit_list = pygame.sprite.spritecollide(fireLaser, alien_private_list, False)
                        for private in alien_private_fire_hit_list:
                            frostLaser_fire_list.remove(fireLaser)
                            private.health = (private.health - hero.damage)
                            all_sprites_list.remove(fireLaser)
                            fireLaser.kill()
                            if private.health <= 0:
                                score += 100
                                if private.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (private.rect.x + 20), (private.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #2)Hero - sergeant alien missile collision
                        alien_sergeant_fire_hit_list = pygame.sprite.spritecollide(fireLaser, alien_sergeant_list, False)
                        for sergeant in alien_sergeant_fire_hit_list:
                            fireLaser_fire_list.remove(fireLaser)
                            sergeant.health = (sergeant.health - hero.damage)
                            all_sprites_list.remove(fireLaser)
                            fireLaser.kill()
                            if sergeant.health <= 0:
                                score += 200
                                if sergeant.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (sergeant.rect.x + 20), (sergeant.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #3)Hero - captain alien missile collision
                        alien_captain_fire_hit_list = pygame.sprite.spritecollide(fireLaser, alien_captain_list, False)
                        for captain in alien_captain_fire_hit_list:
                            fireLaser_fire_list.remove(fireLaser)
                            captain.health = (captain.health - hero.damage)
                            all_sprites_list.remove(fireLaser)
                            fireLaser.kill()
                            if captain.health <= 0:
                                score += 500
                                if captain.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (captain.rect.x + 20), (captain.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                            
                        #4)Hero - boss Bat alien missile collision
                        alien_bossBat_fire_hit_list = pygame.sprite.spritecollide(fireLaser, alien_bossBat_list, False)
                        if alien_bossBat_fire_hit_list:
                            fireLaser_fire_list.remove(fireLaser)
                            bossBat.health = (bossBat.health - hero.damage)
                            all_sprites_list.remove(fireLaser)
                            fireLaser.kill()
                            if bossBat.health <= 0:
                                score += 1000
                                if bossBat.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossBat.rect.x + 20), (bossBat.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                
                                victory += 1
                                bossBati = 0
                                all_sprites_list.remove(bossBat)
                                alien_bossBat_list.remove(bossBat)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossBatdead = 1
                                
                        #5)hero - boss General alien missile collision
                        alien_bossGeneral_fire_hit_list = pygame.sprite.spritecollide(fireLaser, alien_bossGeneral_list, False)
                        if alien_bossGeneral_fire_hit_list:
                            fireLaser_fire_list.remove(fireLaser)
                            bossGeneral.health = (bossGeneral.health - hero.damage)
                            all_sprites_list.remove(fireLaser)
                            fireLaser.kill()
                            if bossGeneral.health <= 0:
                                score += 1500
                                if bossGeneral.spawnDrop():
                                    dropType = random.randrange(1,8)
                                    if dropType == 1:
                                        stamina = StaminaDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(stamina)
                                        stamina_drop_list.add(stamina)
                                        staminaDropi = 1
                                    elif dropType == 2:
                                        heal = HealDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(heal)
                                        heal_drop_list.add(heal)
                                        healDropi = 1
                                    elif dropType == 3:
                                        tenacity = TenacityDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(tenacity)
                                        tenacity_drop_list.add(tenacity)
                                        tenacityDropi = 1
                                    elif dropType == 4:
                                        nanoshell = NanoshellDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(nanoshell)
                                        nanoshell_drop_list.add(nanoshell)
                                        nanoshellDropi = 1
                                    elif dropType == 5:
                                        bullet = BulletDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(bullet)
                                        bullet_drop_list.add(bullet)
                                        bulletDropi = 1
                                    elif dropType == 6:
                                        fstLaser = FrostLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(fstLaser)
                                        frostLaser_drop_list.add(fstLaser)
                                        frostLaserDropi = 1
                                    elif dropType == 7:
                                        freLaser = FireLaserDrop(display_width, display_height, (bossGeneral.rect.x + 20), (bossGeneral.rect.y + 20))
                                        all_sprites_list.add(freLaser)
                                        fireLaser_drop_list.add(freLaser)
                                        fireLaserDropi = 1
                                
                                victory += 1
                                bossGenerali = 0
                                all_sprites_list.remove(bossGeneral)
                                alien_bossGeneral_list.remove(bossGeneral)

                                if game_stage < 3:
                                    game_stage += 1
                                    print_stageflag = 1
                                    bossGeneraldead = 1
                        
                        # Remove hero's missile if goes off the boundaries
                        if fireLaser.rect.y < -fireLaser.rect.y:
                            fireLaser_fire_list.remove(fireLaser)
                            all_sprites_list.remove(fireLaser)
                            fireLaser.remove()
            
            #Check the alien's missile status
            #1)Private - hero missile collision
            if privateFired == 1:
                private_hit_list = pygame.sprite.spritecollide(hero, alien_private_fire_list, True)
                if private_hit_list:
                    hero.health = hero.health - (private.damage - (private.damage * (hero.nanoshell/ 100)))
            
            #2)Sergeant - hero missile collision
            if sergeantFired == 1: 
                sergeant_hit_list = pygame.sprite.spritecollide(hero, alien_sergeant_fire_list, True)
                if sergeant_hit_list:
                    hero.health = hero.health - (sergeant.damage - (sergeant.damage * (hero.nanoshell / 100)))
                    hero.slowed = 1
                    hero.slowflag = 0
            
            #3)Captain - hero missile collision       
            if captainFired == 1:
                captain_FireLaser_hit_list = pygame.sprite.spritecollide(hero, alien_captain_FireLaser_fire_list, True)
                if captain_FireLaser_hit_list:
                    hero.health = hero.health - (captain.damage - (captain.damage * (hero.nanoshell / 100)))
                
                captain_FrostLaser_hit_list = pygame.sprite.spritecollide(hero, alien_captain_FrostLaser_fire_list, True)
                if captain_FrostLaser_hit_list:
                    hero.health = hero.health -(captain.damage - (captain.damage * ((hero.nanoshell / 100) + (10 / 100))))
                    hero.slowed = 1
                    hero.slowflah = 0
                    
            #4)Boss Bat - hero missile collision
            if bossBatFired == 1 and bossBati == 1:
                bossBat_FireLaser_hit_list = pygame.sprite.spritecollide(hero, alien_bossBat_FireLaser_fire_list, True)
                if bossBat_FireLaser_hit_list:
                    hero.health = hero.health - (bossBat.damage - (bossBat.damage * (hero.nanoshell / 100)))
                    
                bossBat_FrostLaser_hit_list = pygame.sprite.spritecollide(hero, alien_bossBat_FrostLaser_fire_list, True)
                if bossBat_FrostLaser_hit_list:
                    hero.health = hero.health - (bossBat.damage - (bossBat.damage * (((hero.nanoshell) / 100) + (20 / 100))))
                    hero.slowed = 1
                    hero.slowflag = 0
                    
            #5)Boss General - hero missile collision
            if bossGeneralFired == 1 and bossGenerali == 1:
                bossGeneral_FireLaser_hit_list = pygame.sprite.spritecollide(hero, alien_bossGeneral_FireLaser_fire_list, True)
                if bossGeneral_FireLaser_hit_list:
                    hero.health = hero.health - (bossGeneral.damage - (bossGeneral.damage * (hero.nanoshell / 100)))
                    
                bossGeneral_FrostLaser_hit_list = pygame.sprite.spritecollide(hero, alien_bossGeneral_FrostLaser_fire_list, True)
                if bossGeneral_FrostLaser_hit_list:
                    hero.health = hero.health - (bossBat.damage - (bossBat.damage * (((hero.nanoshell) / 100) + (20 / 100))))
                    hero.slowed = 1
                    hero.slowflah = 0
                    
            #Drops - hero collision
            #Stamina drop - hero collision
            if staminaDropi == 1:
                hero_stamina_hit_list = pygame.sprite.spritecollide(hero, stamina_drop_list, True)
                if hero_stamina_hit_list:
                    if hero.health == hero.stamina:
                        if hero.stamina < 3000:
                            hero.stamina += 200
                            hero.health = hero.stamina
                            if hero.stamina > 3000:
                                hero.health = hero.stamina = 3000
                    elif hero.stamina < 3000:
                        hero.stamina += 200
                        if hero.stamina > 3000:
                            hero.stamina = 3000
                            
            #Heal drop - hero collision
            if healDropi == 1:
                hero_heal_hit_list = pygame.sprite.spritecollide(hero, heal_drop_list, True)
                if hero_heal_hit_list:
                    if hero.health < hero.stamina:
                        hero.health += (hero.stamina * (30 / 100))
                        if hero.health > hero.stamina:
                            hero.health = hero.stamina
                    elif hero.health == hero.stamina:
                        hero.lives += 1
                        
            #Tenacity drop - hero collision
            if tenacityDropi == 1:
                hero_tenacity_hit_list = pygame.sprite.spritecollide(hero, tenacity_drop_list, True)
                if hero_tenacity_hit_list:
                    if hero.tenacity < 40:
                        hero.tenacity += 5
                        if hero.tenacity > 40:
                            hero.tenacity = 40
                    elif hero.tenacity == 40:
                        if hero.speedx < 11:
                            hero.speedx += 1
                            hero.speedy += 1
                            
            #Nanoshell drop - hero collision
            if nanoshellDropi == 1:
                hero_nanoshell_hit_list = pygame.sprite.spritecollide(hero, nanoshell_drop_list, True)
                if hero_nanoshell_hit_list:
                    if hero.nanoshell < 70:
                        hero.nanoshell += 7
                        if hero.nanoshell > 70:
                            hero.nanoshell = 70
                            
            #Bullet drop - hero collision
            if bulletDropi == 1:
                hero_bullet_hit_list = pygame.sprite.spritecollide(hero, bullet_drop_list, True)
                if hero_bullet_hit_list:
                    hero.setWeapon(1)
                    
            #FrostLaser drop - hero collision
            if frostLaserDropi == 1:
                hero_frostLaser_hit_list = pygame.sprite.spritecollide(hero, frostLaser_drop_list, True)
                if hero_frostLaser_hit_list:
                    hero.setWeapon(2)
                    
            #FireLaser drop - hero collision
            if fireLaserDropi == 1:
                hero_fireLaser_hit_list = pygame.sprite.spritecollide(hero, fireLaser_drop_list, True)
                if hero_fireLaser_hit_list:
                    hero.setWeapon(3)
                            
            #Update    
            all_sprites_list.update()

            #Check the game status
            if hero.health <= 0 and hero.lives == 0:
                Game_Over()
                gameOver = True

            #Draw the sprites(hero,aliens,missiles etc...)
            all_sprites_list.draw(gameDisplay)
            draw_text(gameDisplay, 'Stage: ' + str(game_stage), 22, 48, 10)
            draw_text(gameDisplay, 'Score:' + str(score), 20, display_width / 2, 10)
            draw_text(gameDisplay, 'H:' + str(hero.health), 20, 37, display_height - 50)
            draw_text(gameDisplay, 'S:' + str(hero.stamina), 20, 117, display_height - 50)
            draw_text(gameDisplay, 'L:' + str(hero.lives), 20, 200, display_height - 50)
            draw_text(gameDisplay, 'NS:' + str(hero.nanoshell) +'%', 20, 37, display_height - 30)
            draw_text(gameDisplay, 'T:' + str(hero.tenacity) +'%', 20, 108, display_height - 30)
            draw_text(gameDisplay, 'V:' + str(hero.speedx), 20, 195, display_height - 30)
            draw_text(gameDisplay, 'W:' + str(hero.weapon), 20, display_width - 107, display_height - 50)
            draw_text(gameDisplay, 'WL:' + str(hero.powerLevel), 20, display_width - 100, display_height - 30)
            draw_text(gameDisplay, 'D:' + str(hero.damage), 20, display_width - 40, display_height - 50)
            draw_text(gameDisplay, 'DD:' + str(hero.double_damage), 20, display_width - 40, display_height - 30)

            if bossBati == 1 and bossBatdead == 0:
                draw_text(gameDisplay, 'Boss 1: ' +str(bossBat.health), 20, display_width - 150, 1)
                draw_text(gameDisplay, '/'+str(bossBat.stamina), 12, display_width - 50, 1)
            if bossGenerali == 1 and bossGeneraldead == 0:
                draw_text(gameDisplay, 'Boss 2: '+str(bossGeneral.health), 20, display_width - 150, 20)
                draw_text(gameDisplay, '/'+str(bossGeneral.stamina), 12, display_width - 50, 20)

            #Play background music
            if game_stage == 1 and music == 0:
                pygame.mixer.music.load(airborne)
                pygame.mixer.music.play(-1)
                #airborne.play()
                music += 1
            if game_stage == 2 and music == 1:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(deadlocked)
                pygame.mixer.music.play(-1)
                #airborne.stop()
                #deadlocked.play()
                music += 1
            if game_stage == 3 and music == 2:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(finalbattle)
                pygame.mixer.music.play(-1)
                #deadlocked.stop()
                #finalbattle.play()
                music += 1
            if hero.lives == -1:
                pygame.mixer.music.stop()

            if score >=  9000 and score < 9999:
                boss_spawn = 1
                print_stage = 1
            elif score >= 29000 and score < 29999:
                boss_spawn = 1
                print_stage = 1
            elif score >= 59000 and score < 59999:
                boss_spawn = 1
                print_stage = 1

            

            #Print Stage
            if print_stage == 1:
                if boss_spawn == 1:
                    draw_text(gameDisplay, 'Boss Incoming!!! ', 60, display_width / 2, display_height / 2)
                elif boss_spawn == 0:
                    draw_text(gameDisplay, 'Stage:  ' + str(game_stage), 60, display_width / 2, display_height / 2)

                if time.time() - print_stageTime >= 0.0 and print_stageflag == 0:
                    print_stageTime = time.time()
                    print_stageflag = 1
                elif print_stageflag == 1:
                    if time.time() - print_stageTime > print_stageDuration and boss_spawn == 1:
                        print_stage = 0
                        print_stageflag = 0
                        boss_spawn = 0
                    elif time.time() - print_stageTime > print_stageDuration:
                        print_stage = 0
                        print_stageflag = 0
                        stage_check = game_stage

            score += 1
            if stage_check != game_stage:
                print_stage = 1

            if victory == 4:
                pygame.mixer.music.stop()
                game_Won()
                gameOver = True
            
            pygame.display.update()
            clock.tick(FPS)

    game_Loop()
    pygame.quit()
    return