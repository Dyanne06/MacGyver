# -*- coding: Latin-1 -*
'''
Gameplay Mac Gyver -
Explanation: Mac Gyver must take 3 objets for send to sleep the guardian (Murdoc) and exit
otherwise he dies!

Scripts Python
file: macgyver.py, classes.py, constants.py
directory: Pictures, Sounds
'''
import time
import pygame
from pygame.locals import *
from classes import *
from constants import *

#initialisation pygames
pygame.init()

# create an object "Surface" for the gameplay
BOARD_GAME = pygame.display.set_mode((BOARD_SIZE + BORDURE, BOARD_SIZE))
# icon : load image and display
IMG_PERSO = pygame.image.load(PICTURE_ICON)
pygame.display.set_icon(IMG_PERSO)
# title : display
pygame.display.set_caption(TITLE_WINDOW)

# Create the labyrinthe
# LABY_FILE_DATA is the file with the structure of the labyrinthe
the_laby = Labyrinthe(LABY_FILE_DATA)
the_laby.create()

# add elements for help the personnage to exit
the_ks = KitSurvey(the_laby.struct_OK)
the_laby.modify_struct(the_ks.tools['A'], 'A')
the_laby.modify_struct(the_ks.tools['T'], 'T')
the_laby.modify_struct(the_ks.tools['E'], 'E')

# Display the labyrinth
the_laby.show(BOARD_GAME)

# add the heroe
the_mg = Perso(PICTURE_PERSO_RIGHT, the_laby.start[0], the_laby.start[1])
BOARD_GAME.blit(the_mg.perso, ((the_mg.col * SIZE_SPRITE) + BORDURE, the_mg.row * SIZE_SPRITE))

#refresh
pygame.display.flip()

#parameter for play with the keys pressed
pygame.key.set_repeat(100, 10)
#parameter for refresh
pygame.time.Clock().tick(FPS)

#the main game loop
AGAIN = True
while AGAIN:

    for event in pygame.event.get():

        # events of keybord
        if event.type == QUIT:
            AGAIN = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_SPACE:
                AGAIN = False
            elif event.key == K_RIGHT:
                the_mg.move('Right', the_laby.struct)
            elif event.key == K_LEFT:
                the_mg.move('Left', the_laby.struct)
            elif event.key == K_UP:
                the_mg.move('Up', the_laby.struct)
            elif event.key == K_DOWN:
                the_mg.move('Down', the_laby.struct)
            # display the labyrinthe with the new position of personnage
            # the constant BORDURE is for display the elements and message of end
            the_laby.show(BOARD_GAME)
            BOARD_GAME.blit(the_mg.perso, \
                ((the_mg.col * SIZE_SPRITE)+BORDURE, the_mg.row * SIZE_SPRITE))

            # count and display the element caught by MG
            for tool in the_mg.kit:
                nb = the_mg.kit.index(tool) + 1 #the index starts with 0
                gain = pygame.image.load(KITSURVEY[tool])
                BOARD_GAME.blit(gain, (SIZE_SPRITE, SIZE_SPRITE * nb))

            # with the survival kit, mac gyver make a syringe
            if len(the_mg.kit) == len(KITSURVEY):
                img_seringue = pygame.image.load(PICTURE_SERINGUE)
                BOARD_GAME.blit(img_seringue, (SIZE_SPRITE, (NUMBER_SPRITE_SIDE-2)*SIZE_SPRITE))

            pygame.display.flip()

        # Display GameOver
        if the_mg.nb_life != NB_LIFE_PERSO:
            gameover = pygame.image.load(PICTURE_GAMEOVER)
            BOARD_GAME.blit(gameover, (SIZE_SPRITE, SIZE_SPRITE))
            pygame.display.flip()

        # Display pictures and sounds if the heroe won
        if the_mg.nb_life > 1:
            AGAIN = False
            sound = pygame.mixer.Sound(SOUND_WIN)
            sound.play()
            sound.fadeout(2500)
            gamewin = pygame.image.load(PICTURE_YOUWIN)
            BOARD_GAME.blit(gamewin, (SIZE_SPRITE, (NUMBER_SPRITE_SIDE-2)*SIZE_SPRITE))
            pygame.display.flip()
            time.sleep(5)

        # Display pictures and sounds if the heroe lost
        if the_mg.nb_life < 1:
            AGAIN = False
            sound = pygame.mixer.Sound(SOUND_LOSE)
            sound.play()
            gamelose = pygame.image.load(PICTURE_YOULOSE)
            BOARD_GAME.blit(gamelose, (SIZE_SPRITE, (NUMBER_SPRITE_SIDE-2)*SIZE_SPRITE))
            pygame.display.flip()
            time.sleep(5)
