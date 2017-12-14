# -*- coding: Latin-1 -*
'''
Set of classes
'''
import time
import random
import pygame
from pygame.locals import *
from constants import *

class Labyrinthe:
    ''' this class contains the contructor __init__ and 3 methods
    1) self.create for read the file and put it in the array list_struct
    2) self.modify_struct for add another character in the array
    3) self.show for display the labyrithe in the window
    '''

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
					    if f_column == CHAR_LABY['OK'][0]:
						    self.struct_OK.append((n_column, n_row))
			    list_struct.append(row_laby)
			#print(list_struct )
		    self.struct = list_struct

    def modify_struct(self, coord, c_char):
	    self.struct[coord[1]][coord[0]] = c_char

    def show(self, board_game):
	    ''' commentaires'''
	    img_home = pygame.image.load(PICTURE_HOME)
	    wall = pygame.image.load(CHAR_LABY['Wall'][1]).convert()
	    start = pygame.image.load(CHAR_LABY['Start'][1]).convert_alpha()
	    end = pygame.image.load(CHAR_LABY['End'][1]).convert_alpha()
	    aiguille = pygame.image.load(KITSURVEY['A']).convert_alpha()
	    tube = pygame.image.load(KITSURVEY['T']).convert_alpha()
	    ether = pygame.image.load(KITSURVEY['E']).convert_alpha()
	    board_game.blit(img_home, (BORDURE,0))

	    n_row = 0
	    for row in self.struct:
		    n_col = 0
		    for column in row:
			    x = (n_col * SIZE_SPRITE) + BORDURE
			    y = n_row * SIZE_SPRITE
			    if column == 'm':
				    board_game.blit(wall, (x, y))
			    if column == 'a':
				    board_game.blit(end, (x, y))
			    if column == 'd':
				    board_game.blit(start, (x, y))
				    self.start = (n_col, n_row)
			    if column == 'A':
				    board_game.blit(aiguille, (x, y))
			    if column == 'T':
				    board_game.blit(tube, (x, y))
			    if column == 'E':
				    board_game.blit(ether, (x, y))
			    n_col += 1
		    n_row += 1

class Perso:
    """ this class contains the contructor __init__ and 2 methods
    1) self.move : move the personnage (only coordinate of the personna)
    2) self.ctrl_pos :
    """

    def __init__(self, picture, col, row):
	    self.name = NAME_PERSO
	    self.perso = pygame.image.load(picture).convert_alpha()
	    self.col = col # abscissa
	    self.row = row # ordinate
	    self.kit = []
	    self.nb_life = NB_LIFE_PERSO

    def move(self, direction, tab):
        ''' method for move the personnage in the labyrinthe
        This method modify the coordinate of the personna in the labyrinthe
        '''
        if direction == 'Right':
            if self.col < (NUMBER_SPRITE_SIDE - 1):
				# MG can advance if it's not a wall or the bad perso
                if tab[self.row][self.col+1] != CHAR_LABY['Wall'][0]:
                    self.col += 1
                    self.ctrl_pos(tab)
        if direction == 'Left':
            if self.col > 0:
                if tab[self.row][self.col-1] != CHAR_LABY['Wall'][0]:
                    self.col -= 1
                    self.ctrl_pos(tab)
        if direction == 'Up':
            if self.row > 0:
                if tab[self.row-1][self.col] != CHAR_LABY['Wall'][0]:
                    self.row -= 1
                    self.ctrl_pos(tab)
        if direction == 'Down':
            if self.row < (NUMBER_SPRITE_SIDE - 1):
                if tab[self.row+1][self.col] != CHAR_LABY['Wall'][0]:
                    self.row += 1
                    self.ctrl_pos(tab)

    def ctrl_pos(self, tab):
        ''' method for catch a object or make an action if the heroe is on the bad persona
        if he has the 3 elements then he win a life else he lost a life
        '''
        for obj in KITSURVEY.keys():
            if tab[self.row][self.col] == obj:
                sound = pygame.mixer.Sound(SOUND_TAKE)
                sound.play()
                sound.fadeout(2500) #Fondu à 2,5s de la fin de l'objet "son"
                self.kit.append(obj)
                tab[self.row][self.col] = '0'
        if tab[self.row][self.col] == 'a':
            if len(self.kit) == len(KITSURVEY):
                sound = pygame.mixer.Sound(SOUND_SLEEP)
                sound.play()
                time.sleep(1)
                self.nb_life += 1
            else:
                sound = pygame.mixer.Sound(SOUND_CATCH)
                sound.play()
                time.sleep(1)
                self.nb_life -= 1

class KitSurvey:
    """ list of elements for exit
    create with random.choice
    """
    def __init__(self, struct_laby_OK):
        #Return a random element
        self.tools = {'A': random.choice(struct_laby_OK), \
					  'T': random.choice(struct_laby_OK), \
					  'E': random.choice(struct_laby_OK)}
