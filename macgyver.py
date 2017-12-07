# -*- coding: Latin-1 -*

'''
Jeu Mac Gyver - Jeu de Labyrinthe avec saisi d'objets avant de sortir

Script Python
Fichiers: macgyver.py, classes.py, constantes.py

'''
import os
import pygame
from pygame.locals import *

from classes import *
from structure import *

#initialisation all pygames's module
pygame.init()

# create an object "Surface"
board_game = pygame.display.set_mode((board_size, board_size))
#we load images
img_perso = pygame.image.load(picture_perso_right)
#icon
pygame.display.set_icon(img_perso)
#title
pygame.display.set_caption (title_window)

#Génération du plateau de jeu
#laby_struct is a file define in structure
#the objetc Labyrinthe is the structure (list)
laby = Labyrinthe(laby_file_data)
laby.create()
laby.show(board_game)

#Make the personnage
mg = Perso()
mg.position_perso = mg.position_perso.move(laby.start[0],laby.start[1])
board_game.blit(mg.perso, mg.position_perso)

pygame.display.flip()

again = True

#the main game loop
pygame.key.set_repeat(100,10)

while again:

	pygame.time.Clock().tick(TPS)

	#Création du personnage
	#pass

	for event in pygame.event.get():

		if event.type == QUIT:
			again = False
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE or event.key == K_SPACE:
				again = False
			elif event.key == K_RIGHT:
				mg.move('Right', laby.struct)
			elif event.key == K_LEFT:
				mg.move('Left', laby.struct)
			elif event.key == K_UP:
				mg.move('Up', laby.struct)
			elif event.key == K_DOWN:
				mg.move('Down', laby.struct)
			laby.show(board_game)
			board_game.blit(mg.perso, mg.position_perso)
			pygame.display.flip()

#os.system("pause")
