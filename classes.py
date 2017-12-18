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
    1) self.show => for display the labyrithe in the window
    2) self.modify_struct => for add another character in the array
    3) self.add_kit_survey => for add the elements
    '''

    def __init__(self, laby_file):
        '''
        transform the file into a table with a list of list
        '''
        self.start = (0, 0) #initialisation of sprite START unknowed for the moment
        self.struct = []
        self.struct_OK = []
        with open(laby_file, 'r') as f:
            n_row = 0
            for f_row in f:
                row_laby = []
                n_column = 0
                for f_column in f_row:
                    if f_column != '\n':
                        row_laby.append(f_column)
                        if f_column == CHAR_LABY['OK'][0]:
                            self.struct_OK.append((n_column, n_row))
                    n_column += 1
                n_row += 1
                self.struct.append(row_laby)


    def show(self, board_game):
        '''
        Display the table with pictures
        '''
        #Display the background then all the structure
        board_game.blit(PICTURES['BACKGROUND'], (BORDER,0))

        n_row = 0
        for row in self.struct:
            n_col = 0
            for column in row:
                x = (n_col * SIZE_SPRITE) + BORDER
                y = n_row * SIZE_SPRITE
                if column == 'm':
                    board_game.blit(PICTURES['WALL'], (x, y))
                if column == 'a':
                    board_game.blit(PICTURES['END'], (x, y))
                if column == 'd':
                    board_game.blit(PICTURES['START'], (x, y))
                    self.start = (n_col, n_row)
                if column == 'A':
                    board_game.blit(PICTURES['NEEDLE'], (x, y))
                if column == 'T':
                    board_game.blit(PICTURES['TUBE'], (x, y))
                if column == 'E':
                    board_game.blit(PICTURES['ETHER'], (x, y))
                n_col += 1
            n_row += 1

    def modify_struct(self, coord, c_char):
        """ modify the labyrinth with a new character on the position coord (coordinate: x (column), y (row)))
        """
        self.struct[coord[1]][coord[0]] = c_char

    def add_kit_survey(self):
        """ list of elements for exit
        random element is create with random.choice on the array struct_OK (here it's all the position '0')
        """
        self.modify_struct(random.choice(self.struct_OK), 'A')
        self.modify_struct(random.choice(self.struct_OK), 'T')
        self.modify_struct(random.choice(self.struct_OK), 'E')

class Perso:
    """ this class contains the contructor __init__ and 2 methods
    1) self.move : move the personnage (only coordinate of the personna)
    2) self.catch_obj :
    """

    def __init__(self, col, row):
        self.name = NAME_PERSO
        self.perso = PICTURES['HEROE']
        self.col = col # abscissa
        self.row = row # ordinate
        self.kit = []
        self.nb_life = NB_LIFE_PERSO

    def move(self, direction, tab):
        """method for move the personnage in the labyrinthe
        This method modify the coordinate of the personna in the labyrinthe
        """
        if direction == 'Right':
            if self.col < (NUMBER_SPRITE_SIDE - 1):
                # MG can advance if it's not a wall or the bad perso
                if tab[self.row][self.col+1] != CHAR_LABY['Wall'][0]:
                    self.col += 1
                    self.catch_obj(tab)
        if direction == 'Left':
            if self.col > 0:
                if tab[self.row][self.col-1] != CHAR_LABY['Wall'][0]:
                    self.col -= 1
                    self.catch_obj(tab)
        if direction == 'Up':
            if self.row > 0:
                if tab[self.row-1][self.col] != CHAR_LABY['Wall'][0]:
                    self.row -= 1
                    self.catch_obj(tab)
        if direction == 'Down':
            if self.row < (NUMBER_SPRITE_SIDE - 1):
                if tab[self.row+1][self.col] != CHAR_LABY['Wall'][0]:
                    self.row += 1
                    self.catch_obj(tab)

    def catch_obj(self, tab):
        """method for catch a object or make an action if the heroe is on the bad persona
        if he has the 3 elements then he win a life else he lost a life
        """
        for obj in KITSURVEY.keys():
            if tab[self.row][self.col] == obj:
                sound = pygame.mixer.Sound(SOUND['TAKE'])
                sound.play()
                sound.fadeout(2500) #Fondu à 2,5s de la fin de l'objet "son"
                self.kit.append(obj)
                tab[self.row][self.col] = '0'
        if tab[self.row][self.col] == 'a':
            if len(self.kit) == len(KITSURVEY):
                sound = pygame.mixer.Sound(SOUND['SLEEP'])
                sound.play()
                time.sleep(1)
                self.nb_life += 1
                tab[self.row][self.col] = '0'
            else:
                sound = pygame.mixer.Sound(SOUND['CATCH'])
                sound.play()
                time.sleep(1)
                self.nb_life -= 1
                tab[self.row][self.col] = 'a'
