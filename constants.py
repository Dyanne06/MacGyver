# -*- coding: Latin-1 -*
'''
Set of game constants
'''
import pygame

pygame.init()
# General
SIZE_SPRITE = 32
NUMBER_SPRITE_SIDE = 15
BOARD_SIZE = NUMBER_SPRITE_SIDE*SIZE_SPRITE
BORDER = SIZE_SPRITE * 4

BOARD_GAME = pygame.display.set_mode((BOARD_SIZE + BORDER, BOARD_SIZE))
TITLE_WINDOW = "MacGyver - Labyrinthe contre Murdoc"
NAME_PERSO = 'MacGyver'
NB_LIFE_PERSO = 1

#frame per second (speed of program)
FPS = 30

# Pictures
PICTURES = {'HEROE' : pygame.image.load("Pictures/macgyver.png").convert_alpha(),
            'BACKGROUND' : pygame.image.load("Pictures/fond.png"),
            'WALL' : pygame.image.load("Pictures/wall.jpg").convert(),
            'START': pygame.image.load("Pictures/macgyver_trace.png").convert_alpha(),
            'END' : pygame.image.load("Pictures/murdoc.png").convert_alpha(),
            'YOUWIN' : pygame.image.load("Pictures/YouWin.png"),
            'YOULOSE' : pygame.image.load("Pictures/YouLost.png"),
            'TUBE': pygame.image.load("Pictures/tube.png").convert_alpha(),
            'ETHER': pygame.image.load("Pictures/ether.png").convert_alpha(),
            'NEEDLE': pygame.image.load("Pictures/aiguille.png").convert_alpha()}
#Sounds
SOUND = {'WIN' : "Sounds/gong.wav",
         'LOSE' : "Sounds/falling.wav",
         'TAKE' : "Sounds/kongas.wav",
         'SLEEP' : "Sounds/whiff.wav",
         'CATCH' : "Sounds/punch.wav"
         }

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
