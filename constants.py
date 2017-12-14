# -*- coding: Latin-1 -*
'''
Set of game constants
'''
# General
SIZE_SPRITE = 32
NUMBER_SPRITE_SIDE = 15
BOARD_SIZE = NUMBER_SPRITE_SIDE*SIZE_SPRITE
BORDURE = SIZE_SPRITE * 4

TITLE_WINDOW = "MacGyver - Labyrinthe contre Murdoc"
NAME_PERSO = 'MacGyver'
NB_LIFE_PERSO = 1

#frame per second (speed of program)
FPS = 30

# Pictures
PICTURE_ICON = "Pictures/macgyver_right.png"
PICTURE_HOME = "Pictures/fond.png"
PICTURE_FOND = "Pictures/background.png"
PICTURE_PERSO_RIGHT = "Pictures/macgyver_right.png"
#PICTURE_PERSO_LEFT = "Pictures/macgyver_left.png"
PICTURE_BAD_PERSO = "Pictures/murdoc.png"
PICTURE_SERINGUE = "Pictures/seringue.png"

PICTURE_YOUWIN = "Pictures/YouWin.png"
PICTURE_YOULOSE = "Pictures/YouLost.png"
PICTURE_GAMEOVER =  "Pictures/GameOver.png"

#Sounds
SOUND_WIN = "Sounds/gong.wav"
SOUND_LOSE = "Sounds/falling.wav"
SOUND_TAKE = "Sounds/kongas.wav"
SOUND_SLEEP = "Sounds/whiff.wav"
SOUND_CATCH = "Sounds/punch.wav"

# description of file for build a labyrinth
# we can improve with json for later
LABY_FILE_DATA = "FileForGames/laby1"
CHAR_LABY = {'OK': ('0', ""), \
             'Wall': ('m', "Pictures/wall.jpg"), \
             'Start': ('d', "Pictures/macgyver_trace.png"), \
             'End': ('a', "Pictures/murdoc.png")}
KITSURVEY = {'A': "Pictures/aiguille.png", \
             'T': "Pictures/tube.png", \
             'E': "Pictures/ether.png" \
            }
