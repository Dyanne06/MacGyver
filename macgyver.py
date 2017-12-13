# -*- coding: Latin-1 -*
'''
Jeu Mac Gyver - Jeu de Labyrinthe avec saisi d'objets avant de sortir

Script Python
Fichiers: macgyver.py, classes.py, constantes.py

'''
import time
import pygame
from pygame.locals import *
from structure import *
from classes import *

#initialisation all pygames's module
pygame.init()

# create an object "Surface"
BOARD_GAME = pygame.display.set_mode((BOARD_SIZE + BORDURE, BOARD_SIZE))
#we load images
IMG_PERSO = pygame.image.load(PICTURE_ICON)
#icon
pygame.display.set_icon(IMG_PERSO)
#title
pygame.display.set_caption(TITLE_WINDOW)

#Génération du plateau de jeu
#laby_struct is a file define in structure
#the objetc Labyrinthe is the structure (list)
the_laby = Labyrinthe(LABY_FILE_DATA)
the_laby.create()
#laby.show(board_game)

#Create elements
the_ks = KitSurvey(the_laby.struct_OK)
the_laby.modify_struct(the_ks.tools['A'], 'A')
the_laby.modify_struct(the_ks.tools['T'], 'T')
the_laby.modify_struct(the_ks.tools['E'], 'E')
the_laby.show(BOARD_GAME)

#Make the personnag
the_mg = Perso(PICTURE_PERSO_RIGHT, the_laby.start[0], the_laby.start[1])
BOARD_GAME.blit(the_mg.perso, ((the_mg.col * SIZE_SPRITE) + BORDURE, the_mg.row * SIZE_SPRITE))

#refresh
pygame.display.flip()

#the main game loop
AGAIN = True
pygame.key.set_repeat(100, 10)

while AGAIN:

    pygame.time.Clock().tick(FPS)

    for event in pygame.event.get():

        if event.type == QUIT:
            again = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_SPACE:
                again = False
            elif event.key == K_RIGHT:
                the_mg.move('Right', the_laby.struct)
            elif event.key == K_LEFT:
                the_mg.move('Left', the_laby.struct)
            elif event.key == K_UP:
                the_mg.move('Up', the_laby.struct)
            elif event.key == K_DOWN:
                the_mg.move('Down', the_laby.struct)
            the_laby.show(BOARD_GAME)
            BOARD_GAME.blit(the_mg.perso, \
                ((the_mg.col * SIZE_SPRITE)+BORDURE, the_mg.row * SIZE_SPRITE))
            nb = 0

            for tool in the_mg.kit:
                gain = pygame.image.load(KITSURVEY[tool])
                nb = the_mg.kit.index(tool) + 1
                BOARD_GAME.blit(gain, (SIZE_SPRITE, SIZE_SPRITE * nb))

            if nb == 3:
                img_seringue = pygame.image.load(PICTURE_SERINGUE)

            pygame.display.flip()

        if the_mg.nb_life > 1:
            AGAIN = False
            son = pygame.mixer.Sound("sons/gong.wav")
            son.play()
            son.fadeout(2500)
            BOARD_GAME.blit(img_seringue, (SIZE_SPRITE, (NUMBER_SPRITE_SIDE-2)*SIZE_SPRITE))
            pygame.display.flip()
            time.sleep(5)
            #Improve: Display a win game

        if the_mg.nb_life < 1:
            AGAIN = False
            son = pygame.mixer.Sound("sons/falling.wav")
            son.play()
            time.sleep(5)
    #Afficher un game over
