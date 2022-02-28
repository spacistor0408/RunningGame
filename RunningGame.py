import cv2
import HandTrackingModule as HandTracker
import HandDetectController
import DinoGameControl
from pygame import time
# import pygame
# import os
# import random

#pygame.init()

FPS = 30

def main():

    cap = cv2.VideoCapture(0)
    detector = HandTracker.HandDetector( maxHands=1 )
    gestureController = HandDetectController.GestureController()

    run = True
    DinoGame = DinoGameControl.DinoGame()
    clock = time.Clock()
    # player = Dinosaur()
    # cloud = Cloud()
    # bg = BackGround()
    
    # global GAMESPEED
    # GAMESPEED = 0

    while run:
        
        # Get Input
        clock.tick(FPS)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        # SCREEN.fill( WHITE )

        # Set Game FPS

        run = DinoGame.IsExist()
        
        success, img = cap.read()

        img = cv2.flip(img, 1)
        img = detector.FindHands(img, draw = True)
        handLandMarkPosition = detector.GetPosition(img, draw = False)

        # hand gesture

        if success:

            cv2.putText(img, str(int(gestureController.GetFPS())), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (151, 166, 134), 3)

            #if len(handLandMarkPosition) != 0 :
                
            gestureController.Update(img, *handLandMarkPosition)
            

            cv2.putText( img, str(int(gestureController.GetStep())), ( 100, 70 ), cv2.FONT_HERSHEY_PLAIN, 3, ( 156, 53, 58 ), 3 )
            cv2.imshow('img', img)

        #GameSpeed = gestureController.GetVelocity()*10
            DinoGame.SetSpeed(gestureController.GetVelocity()*10)
            DinoGame.SetPlayerState(gestureController.GetHandGesture())
            # UPDATE

            DinoGame.UpDate()

        # player.Draw()
        # player.Update()
        # cloud.Draw()
        # cloud.Update()
        # bg.Draw()
        # bg.Update()

        # Display
        #pygame.display.update()


        if cv2.waitKey(1) == ord('q'):
            run = False


if __name__ == '__main__':
    main() 
