# -*- coding: Latin-1 -*
'''
Liste des classes d'objets pour le jeu MacGyver

'''

import pygame
import random
from pygame.locals import *
from structure import *

class Labyrinthe:
	''' classe pour créer le labyrinthe'''

	def __init__(self, fichier):
		self.fichier = fichier
		self.struct = []
		self.struct_OK = []
		self.start = (0,0)

	def create(self):
		'''commentaires'''
		with open(self.fichier,'r') as f:
			list_struct = []
			n_row = -1
			for f_row in f:
				row_laby = []
				n_row += 1
				n_column = -1
				for f_column in f_row:
					if f_column !='\n':
						row_laby.append(f_column)
						n_column +=1
						if f_column == char_zero:
							self.struct_OK.append((n_column, n_row))
				list_struct.append(row_laby)
			#print(list_struct )
			self.struct = list_struct

	def modify_struct(self, coord_tool, c_char):
		self.struct[coord_tool[1]][coord_tool[0]] = c_char

	def show(self, board_game):
		''' commentaires'''
		img_home = pygame.image.load(picture_home)

		wall = pygame.image.load(picture_wall).convert()
		start = pygame.image.load(picture_start).convert_alpha()
		end = pygame.image.load(picture_end).convert_alpha()
		seringue = pygame.image.load(picture_seringue).convert_alpha()
		tube = pygame.image.load(picture_tube).convert_alpha()
		ether = pygame.image.load(picture_ether).convert_alpha()


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
				if column == char_tools['seringue']:
					board_game.blit(seringue, (x,y))
				if column == char_tools['tube']:
					board_game.blit(tube, (x,y))
				if column == char_tools['ether']:
					board_game.blit(ether, (x,y))
				n_col += 1
			n_row += 1

class Perso:
	'''Class of personnage'''

	def __init__(self, picture, col, row):
		self.name = name_perso
		self.perso = pygame.image.load(picture).convert_alpha()
		self.col = col # abscisse
		self.row = row # ordonnée
		self.kit = []
		self.nb_life = nb_life_perso

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
				# MG can advance if it's not a wall or the bad perso
				if tab[self.row][self.col+1] != char_wall:
					self.col += 1
					self.ctrl_pos(self.col, self.row)

		if direction == 'Left':
			if self.col > 0:
				if tab[self.row][self.col-1] != char_wall:
					self.col -= 1
					self.ctrl_pos(self.col, self.row)

		if direction == 'Up':
			if self.row > 0:
				if tab[self.row-1][self.col] != char_wall:
					self.row -= 1
					self.ctrl_pos(self.col, self.row)

		if direction == 'Down':
			if self.row < (number_sprite_side - 1):
				if tab[self.row+1][self.col] != char_wall:
					self.row += 1
					self.ctrl_pos(self.col, self.row)

	def ctrl_pos(self, abs, coord):
		pass

class KitSurvey:
	""" list of elements in order to exit"""
	def __init__(self, struct_laby_OK):
		self.tools = {'seringue': random.choice(struct_laby_OK), \
					  'tube': random.choice(struct_laby_OK), \
					  'ether': random.choice(struct_laby_OK)}
		#self.tool2 =
		#self.tool3 = KITSURVEY('')

	def display_tools_random(self):
		# on modifie la structure du labyrinthe pour y rajouter les outils

		for i in struct_laby_OK:
			pass
