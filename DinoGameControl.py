
import pygame
import random
import cfg


pygame.init()
SCREEN = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))

class Dinosaur():

    DinoXPos = 80
    DinoYPos = 310
    JumpingPlacement = 30
    FallingVelocity = 2

    def __init__(self):
        self.run_img = []
        for value in cfg.IMAGES['RUNNING']:
            self.run_img.append(pygame.image.load(value)) # loading the running image
        self.jump_img = pygame.image.load( cfg.IMAGES['JUMPING'] ) # loading the jumping image

        self.run_state = True
        self.jump_state = False

        self.curJumpingVelocity = self.JumpingPlacement
        self.step_index = 0 # record step to switch run1 and run2 image
        self.display_img = self.run_img[0]


    def Update(self, speed ):
        if self.run_state :
            self.Run( speed )

        if self.jump_state :
            self.Jump()

        if ( self.step_index >= 10 ): # switch running image 2 to running image 1
            self.step_index = 0


    def Run(self, speed ):
        self.display_img = self.run_img[ self.step_index // 5 ]
        if ( speed > 1 ): # To decide weather the running image need to switch
            self.step_index += 1


    def Jump(self):
        # switch to jumping image
        self.display_img = self.jump_img

        self.DinoYPos -= self.curJumpingVelocity
        self.curJumpingVelocity -= self.FallingVelocity

        # if Dino is Falling to the ground, then stop falling 
        if ( self.curJumpingVelocity < -self.JumpingPlacement ):
            self.curJumpingVelocity = self.JumpingPlacement
            self.jump_state = False

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

class Bird():
    def __init__(self):
        self.xPos = cfg.SCREEN_WIDTH
        self.yPos = 250
        self.fly_img = []

        for value in cfg.IMAGES['BIRD']:
            self.fly_img.append(pygame.image.load(value))

        self.display_img = self.fly_img[0]
        self.fly_index = 0
        self.flyingSpeed = 5

    def Update( self, speed ):
        self.xPos -= (self.flyingSpeed + speed)
        if ( self.xPos <= -self.display_img.get_width() ):
            self.xPos = cfg.SCREEN_WIDTH + random.randint(100, 2000)
            self.yPos = random.randint( 250, 270 )
        
        self.Fly()
        if ( self.fly_index >= 10 ):
            self.fly_index = 0

        #print( self.xPos, self.yPos )

    def Fly( self ):
        self.display_img = self.fly_img[ self.fly_index//5 ]
        self.fly_index += 1

    def Draw(self):
        SCREEN.blit( self.display_img, (self.xPos, self.yPos) )

class LargeCactus():
    def __init__(self):
        
        self.xPos = cfg.SCREEN_WIDTH
        self.yPos = cfg.GROUND_HEIGHT1

        self.cactus_img = []
        for value in cfg.IMAGES['LARGE_CACTUS']:
            self.cactus_img.append(pygame.image.load(value))

        self.cactusNumber = random.randint(0, 2)
        self.display_img = self.cactus_img[self.cactusNumber]
        
    def Update(self, speed):
        self.xPos -= speed
        if ( self.xPos <= -self.display_img.get_width() ):
            self.xPos = cfg.SCREEN_WIDTH + random.randint(100, 1000)
            self.cactusNumber = random.randint(0, 2)
            self.display_img = self.cactus_img[self.cactusNumber]

    def Draw(self):
        SCREEN.blit(self.display_img, (self.xPos, self.yPos))

class SmallCactus():
    def __init__(self):
        
        self.xPos = random.randint(100, cfg.SCREEN_WIDTH)
        self.yPos = cfg.GROUND_HEIGHT1

        self.cactus_img = []
        for value in cfg.IMAGES['SMALL_CACTUS']:
            self.cactus_img.append(pygame.image.load(value))

        self.cactusNumber = random.randint(0, 2)
        self.display_img = self.cactus_img[self.cactusNumber]
        
    def Update(self, speed):
        self.xPos -= speed
        if ( self.xPos <= -self.display_img.get_width() ):
            self.xPos = cfg.SCREEN_WIDTH + random.randint(100, 1000)
            self.cactusNumber = random.randint(0, 2)
            self.display_img = self.cactus_img[self.cactusNumber]

    def Draw(self):
        SCREEN.blit(self.display_img, (self.xPos, self.yPos))

class DinoGame():

    def __init__(self): 
        self.GAMESPEED = 0
        self.clock = pygame.time.Clock()

        self.player = Dinosaur()
        self.cloud = Cloud()
        self.bg = BackGround()
        self.bird = Bird()
        self.smallCactus1 = SmallCactus()
        self.largeCactus1 = LargeCactus()

        SCREEN.fill(cfg.COLOR)

    def UpDate(self):
        SCREEN.fill(cfg.COLOR)
        self.player.Draw()
        self.player.Update( self.GAMESPEED )
        self.cloud.Draw()
        self.cloud.Update( self.GAMESPEED )
        self.bg.Draw()
        self.bg.Update( self.GAMESPEED )
        self.bird.Draw()
        self.bird.Update(self.GAMESPEED)
        self.smallCactus1.Draw()
        self.smallCactus1.Update( self.GAMESPEED )
        self.largeCactus1.Draw()
        self.largeCactus1.Update( self.GAMESPEED )

        pygame.display.update()

    def SetSpeed(self, speed):
        self.GAMESPEED = speed

    def SetPlayerState(self, handGesture):
        #print( handGesture )
        if ( handGesture == "JUMPING" ):
            self.player.jump_state = True

    def IsExist(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True