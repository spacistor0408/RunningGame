import os

PATH = "Assets/"

IMAGES = {
    'RUNNING':[os.path.join( PATH, "Dino/DinoRun1.png"), 
               os.path.join( PATH, "Dino/DinoRun2.png") ], 

    'JUMPING':os.path.join( PATH, "Dino/DinoJump.png"),

    'DUNKING':[os.path.join( PATH, "Dino/DinoDuck1.png"), 
               os.path.join( PATH, "Dino/DinoDuck2.png")], 

    'SMALL_CACTUS':[os.path.join( PATH, "Catus/SmallCactus1.png"), 
                    os.path.join( PATH, "Catus/SmallCactus2.png"),
                    os.path.join( PATH, "Catus/SmallCactus3.png")],

    'LARGE_CACTUS':[os.path.join( PATH, "Catus/LargeCactus1.png"),
                    os.path.join( PATH, "Catus/LargeCactus2.png"),
                    os.path.join( PATH, "Catus/LargeCactus3.png")],

    'BIRD':[os.path.join( PATH, "Bird/Bird1.png"), 
            os.path.join( PATH, "Bird/Bird2.png")],

    'CLOUD':os.path.join( PATH, "Other/Cloud.png"),

    'BG':os.path.join( PATH, "Other/Track.png"),

    'GAMEOVER':os.path.join( PATH, "Other/GameOver.png"),

    'Reset':os.path.join( PATH, "Other/Reset.png")
}


# Game Setting

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100 

WHITE = (255, 255, 255)
COLOR = WHITE
FPS = 30