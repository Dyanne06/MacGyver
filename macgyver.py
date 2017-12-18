# -*- coding: Latin-1 -*
# pylint: disable=C0103
'''
Gameplay Mac Gyver -
Explanation: Mac Gyver must take 3 objets
for send to sleep the guardian (Murdoc) and exit
otherwise he dies!

Scripts Python
file: macgyver.py, classes.py, constants.py
directory: Pictures, Sounds
'''
import time
import pygame
from pygame.locals import *
from classes import Labyrinthe, Perso
from constants import *

#initialisation pygames
pygame.display.init()

# icon :
pygame.display.set_icon(PICTURES['HEROE'])
# title :
pygame.display.set_caption(TITLE_WINDOW)

# Create the labyrinthe
# LABY_FILE_DATA is the file with the structure of the labyrinthe
laby = Labyrinthe(LABY_FILE_DATA)
# add elements for help the personnage to exit
laby.add_kit_survey()
# Display the labyrinth
laby.show(BOARD_GAME)

# add the heroe
mg = Perso(laby.start[0], laby.start[1])
# Display the heroe on the surface
BOARD_GAME.blit(mg.perso, ((mg.col * SIZE_SPRITE) + BORDER, \
                            mg.row * SIZE_SPRITE))

#refresh
pygame.display.flip()

#parameter for play with the keys pressed
pygame.key.set_repeat(100, 10)
#parameter for refresh
pygame.time.Clock().tick(FPS)

#the main game loop
AGAIN = True
while AGAIN: #boucle d'événements

    for event in pygame.event.get(): #Parcours de la liste des événements

        # events of keybord
        if event.type == QUIT:
            AGAIN = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_SPACE:
                AGAIN = False
            elif event.key == K_RIGHT:
                mg.move('Right', laby.struct)
            elif event.key == K_LEFT:
                mg.move('Left', laby.struct)
            elif event.key == K_UP:
                mg.move('Up', laby.struct)
            elif event.key == K_DOWN:
                mg.move('Down', laby.struct)
            # display the labyrinthe with the new position of personnage
            # the constant BORDER is for display the elements
            # and message of end
            laby.show(BOARD_GAME)
            BOARD_GAME.blit(mg.perso, \
                ((mg.col * SIZE_SPRITE)+BORDER, mg.row * SIZE_SPRITE))

            # count and display the element caught by MG
            for tool in mg.kit:
                nb = mg.kit.index(tool) + 1 #the index starts with 0
                gain = pygame.image.load(KITSURVEY[tool])
                BOARD_GAME.blit(gain, (SIZE_SPRITE, SIZE_SPRITE * nb))

            pygame.display.flip()

        # Display pictures and sounds if the heroe won
        if mg.nb_life > 1:
            AGAIN = False
            sound = pygame.mixer.Sound(SOUND['WIN'])
            sound.play()
            sound.fadeout(2500)
            BOARD_GAME.blit(PICTURES['YOUWIN'], \
                        (SIZE_SPRITE, (NUMBER_SPRITE_SIDE/2)*SIZE_SPRITE))
            pygame.display.flip()
            time.sleep(5)

        # Display pictures and sounds if the heroe lost
        if mg.nb_life < 1:
            AGAIN = False
            sound = pygame.mixer.Sound(SOUND['LOSE'])
            sound.play()
            BOARD_GAME.blit(PICTURES['YOULOSE'], \
                        (SIZE_SPRITE, (NUMBER_SPRITE_SIDE/2)*SIZE_SPRITE))
            laby.show(BOARD_GAME)
            pygame.display.flip()
            time.sleep(5)
