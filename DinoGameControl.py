
import pygame
import random
import cfg


pygame.init()
SCREEN = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))

class Dinosaur():

    DinoXPos = 80
    DinoYPos = 310

    def __init__(self):
        self.run_img = []
        for value in cfg.IMAGES['RUNNING']:
            self.run_img.append(pygame.image.load(value)) 

        self.run_state = True
        self.step_index = 0 # record step to switch run1 and run2 image

        self.display_img = self.run_img[0]


    def Update(self, speed ):
        if ( self.run_state == True ):
            self.Run( speed )

        if ( self.step_index >= 10 ):
            self.step_index = 0


    def Run(self, speed ):
        self.display_img = self.run_img[ self.step_index // 5 ]
        if ( speed > 1 ):
            self.step_index += 1

    def Draw(self):
        SCREEN.blit( self.display_img, ( self.DinoXPos, self.DinoYPos ) )

class Cloud():
    def __init__(self):
        self.xPos = cfg.SCREEN_HEIGHT + random.randint(800, 1000)
        self.yPos = random.randint(50, 100)
        self.display_img = pygame.image.load(cfg.IMAGES['CLOUD'])
        self.width = self.display_img.get_width()

    def Update(self, speed):
        self.xPos -= speed
        if ( self.xPos < -self.width ):
            self.xPos = cfg.SCREEN_WIDTH + random.randint(800, 2000)
            self.yPos = random.randint(50, 100)

    def Draw(self):
        SCREEN.blit(self.display_img, (self.xPos, self.yPos))

class BackGround():
    def __init__(self):
        self.xPos = 0
        self.yPos = 380
        self.display_img = pygame.image.load(cfg.IMAGES['BG'])
        self.width = self.display_img.get_width() 

    def Update(self, speed):
        self.xPos -= speed
        if ( self.xPos <= -self.width ):
            self.xPos = 0

    def Draw(self):
        SCREEN.blit(self.display_img, (self.xPos, self.yPos))
        SCREEN.blit(self.display_img, (self.width + self.xPos, self.yPos))

class DinoGame():

    def __init__(self): 
        self.GAMESPEED = 0
        self.clock = pygame.time.Clock()

        self.player = Dinosaur()
        self.cloud = Cloud()
        self.bg = BackGround()
        SCREEN.fill(cfg.COLOR)

    def UpDate(self):
        SCREEN.fill(cfg.COLOR)
        self.player.Draw()
        self.player.Update( self.GAMESPEED )
        self.cloud.Draw()
        self.cloud.Update( self.GAMESPEED )
        self.bg.Draw()
        self.bg.Update( self.GAMESPEED )

        pygame.display.update()

    def SetSpeed(self, speed):
        self.GAMESPEED = speed

    def IsExist(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True