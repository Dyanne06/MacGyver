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
					self.start = (x,y)
				n_col += 1
			n_row += 1

class Perso:
	'''Class of personnage'''

	def __init__(self):
		self.name = name_perso
		self.perso = pygame.image.load(picture_perso_right).convert_alpha()
		self.position_perso = self.perso.get_rect()

	def x_translate(self):
		col = 0
		row = 0
		x = self.position_perso[0]
		y = self.position_perso[1]
		if x != 0:
			col = int(x/size_sprite)
		if y != 0:
			row = int(y/size_sprite)
		return col

	def y_translate(self):
		y = self.position_perso.move(size_sprite, 0)[1]
		if y != 0:
			return int(y/size_sprite)
		else:
			return 0

	def move(self, direction, tab):
		''' move the personnage '''
		if direction == 'Right':
			col = self.x_translate()+1
			row = self.y_translate()
			if col < number_sprite_side and (tab[row][col] == char_start or tab[row][col] == char_zero):
				self.position_perso = self.position_perso.move(size_sprite, 0)
				self.perso = pygame.image.load(picture_perso_right).convert_alpha()
		if direction == 'Left':
			col = self.x_translate()-1
			row = self.y_translate()
			if (col >=0) and (tab[row][col] == char_start or tab[row][col] == char_zero):
				self.position_perso = self.position_perso.move(-size_sprite, 0)
				self.perso = pygame.image.load(picture_perso_left).convert_alpha()
		if direction == 'Up':
			col = self.x_translate()
			row = self.y_translate()-1
			if row >= 0 and (tab[row][col] == char_start or tab[row][col] == char_zero):
				self.position_perso = self.position_perso.move(0, -size_sprite)
				self.perso = pygame.image.load(picture_perso_right).convert_alpha()
		if direction == 'Down':
			col = self.x_translate()
			row = self.y_translate()+1
			if row < number_sprite_side and (tab[row][col] == char_start or tab[row][col] == char_zero):
				self.position_perso = self.position_perso.move(0, size_sprite)
				self.perso = pygame.image.load(picture_perso_right).convert_alpha()
