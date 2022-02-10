import cv2
import HandTrackingModule as HandTracker
import GameController
import pygame
import os
import random

pygame.init()

FPS = 30

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

WHITE = (255, 255, 255)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


RUNNING = [pygame.image.load(os.path.join('Assets/Dino/DinoRun1.png')), 
           pygame.image.load(os.path.join("Assets/Dino/DinoRun2.png")) ]
# JUMPING = pygame.image.load(os.path.join("Assets/Dino/DinoJump.png"))
# DUNKING = [pygame.image.load(os.path.join("Assets/Dino/DinoDuck1.png")), 
#            pygame.image.load(os.path.join("Assets/Dino/DinoDuck1.png"))]

CLOUD = pygame.image.load(os.path.join('Assets/Other/Cloud.png'))
BG = pygame.image.load(os.path.join('Assets/Other/Track.png'))

class Dinosaur():

    DinoXPos = 80
    DinoYPos = 310

    def __init__(self):
        self.run_img = RUNNING
        self.run_state = True
        self.step_index = 0 # record step to switch run1 and run2 image

        self.display_img = self.run_img[0]


    def Update(self ):
        if ( self.run_state == True ):
            self.Run()

        if ( self.step_index >= 10 ):
            self.step_index = 0


    def Run(self):
        self.display_img = self.run_img[ self.step_index // 5 ]
        if ( GAMESPEED > 1 ):
            self.step_index += 1

    def Draw(self ):
        SCREEN.blit( self.display_img, ( self.DinoXPos, self.DinoYPos ) )

class Cloud():
    def __init__(self):
        self.xPos = SCREEN_HEIGHT + random.randint(800, 1000)
        self.yPos = random.randint(50, 100)
        self.display_img = CLOUD
        self.width = self.display_img.get_width()

    def Update(self):
        self.xPos -= GAMESPEED
        if ( self.xPos < -self.width ):
            self.xPos = SCREEN_WIDTH + random.randint(800, 2000)
            self.yPos = random.randint(50, 100)

    def Draw(self):
        SCREEN.blit(self.display_img, (self.xPos, self.yPos))

class BackGround():
    def __init__(self):
        self.xPos = 0
        self.yPos = 380
        self.display_img = BG
        self.width = self.display_img.get_width()
        

    def Update(self):
        self.xPos -= GAMESPEED
        if ( self.xPos <= -self.width ):
            self.xPos = 0

    def Draw(self):
        SCREEN.blit(self.display_img, (self.xPos, self.yPos))
        SCREEN.blit(self.display_img, (self.width + self.xPos, self.yPos))

def main():

    cap = cv2.VideoCapture(0)
    detector = HandTracker.HandDetector( )
    controller = GameController.GameControl()

    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    bg = BackGround()
    
    global GAMESPEED
    GAMESPEED = 0
    
    while run:
        
        # Get Input
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill( WHITE )


        success, img = cap.read()

        img = cv2.flip(img, 1)
        img = detector.FindHands(img, True)
        handLandMarkPosition = detector.GetPosition(img)

        # hand gesture
        if success:

            cv2.putText(img, str(int(controller.GetFPS())), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (151, 166, 134), 3)

            #if len(handLandMarkPosition) != 0 :
                
            controller.Run(img, *handLandMarkPosition)
            cv2.putText( img, str(int(controller.GetStep())), ( 100, 70 ), cv2.FONT_HERSHEY_PLAIN, 3, ( 156, 53, 58 ), 3 )
            cv2.imshow('img', img)

        GAMESPEED = controller.GetVelocity()*10

        # UPDATE
        player.Draw()
        player.Update()
        cloud.Draw()
        cloud.Update()
        bg.Draw()
        bg.Update()

        # Display
        pygame.display.update()


        if cv2.waitKey(1) == ord('q'):
            run = False


if __name__ == '__main__':
    main() 
