# -*- coding: Latin-1 -*
'''
Liste des classes d'objets pour le jeu MacGyver

'''

import pygame
from pygame.locals import *
from structure import *

class Labyrinthe:
	''' classe pour créer le labyrinthe'''

	def __init__(self, fichier):
		self.fichier = fichier
		self.struct = []
		self.start = (0,0)

	def create(self):
		'''commentaires'''
		with open(self.fichier,'r') as f:
			list_struct = []
			for f_row in f:
				row_laby = []
				for f_column in f_row:
					if f_column !='\n':
						row_laby.append(f_column)
				list_struct.append(row_laby)
			#print(list_struct )
			self.struct = list_struct

	def show(self, board_game):
		''' commentaires'''
		img_home = pygame.image.load(picture_home)

		wall = pygame.image.load(picture_wall).convert()
		start = pygame.image.load(picture_start).convert_alpha()
		end = pygame.image.load(picture_end).convert_alpha()

		board_game.blit(img_home, (0,0))

		n_row = 0
		for row in self.struct:
			n_col = 0
			for column in row:
				x = n_col * size_sprite
				y = n_row * size_sprite
				if column == 'm':
					board_game.blit(wall, (x,y))
				if column == 'a':
					board_game.blit(end, (x,y))
				if column == 'd':
					board_game.blit(start, (x,y))
					self.start = (n_col,n_row)
				n_col += 1
			n_row += 1

class Perso:
	'''Class of personnage'''

	def __init__(self, col, row):
		self.name = name_perso
		self.perso = pygame.image.load(picture_perso_right).convert_alpha()
		self.col = col # abscisse
		self.row = row # ordonnée

	def x_translate(self):
		x = self.col * size_sprite
		return x

	def y_translate(self):
		y = self.row * size_sprite
		return y

	def move(self, direction, tab):
		''' move the personnage '''
		if direction == 'Right':
			if self.col < (number_sprite_side - 1):
				if tab[self.row][self.col+1] == char_start or tab[self.row][self.col+1] == char_zero:
					self.col += 1
		if direction == 'Left':
			if self.col > 0:
				if tab[self.row][self.col-1] == char_start or tab[self.row][self.col-1] == char_zero:
					self.col -= 1
		if direction == 'Up':
			if self.row > 0:
				if tab[self.row-1][self.col] == char_start or tab[self.row-1][self.col] == char_zero:
					self.row -= 1
		if direction == 'Down':
			if self.row < (number_sprite_side - 1):
				if tab[self.row+1][self.col] == char_start or tab[self.row+1][self.col] == char_zero:
					self.row += 1
