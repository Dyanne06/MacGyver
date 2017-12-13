# -*- coding: Latin-1 -*
'''
structure du jeu (départ, emplacement des murs, arrivée)
'''
# General
SIZE_SPRITE = 32
NUMBER_SPRITE_SIDE = 15
BOARD_SIZE = NUMBER_SPRITE_SIDE*SIZE_SPRITE
BORDURE = SIZE_SPRITE * 4

#
TITLE_WINDOW = "MacGyver - Labyrinthe contre Murdoc"

NAME_PERSO = 'MacGyver'
NB_LIFE_PERSO = 1

#frame per second (speed of program)
FPS = 30

# list of Images
PICTURE_ICON = "images/macgyver.png"
PICTURE_HOME = "images/fond.png"
PICTURE_FOND = "images/background.jpg"
PICTURE_PERSO_RIGHT = "images/macgyver_right.png"
#PICTURE_PERSO_LEFT = "images/macgyver_left.png"
PICTURE_BAD_PERSO = "images/murdoc.png"
PICTURE_SERINGUE = "images/seringue.png"

#description of file for build a labyrinth
LABY_FILE_DATA = "images/laby1"
CHAR_LABY = {'OK': ('0', ""), \
             'Wall': ('m', "images/mur.jpg"), \
             'Start': ('d', "images/macgyver_trace.png"), \
             'End': ('a', "images/murdoc.png")}
KITSURVEY = {'A': "images/aiguille.png", \
             'T': "images/tube.png", \
             'E': "images/ether.png" \
            }
