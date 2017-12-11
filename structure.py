# -*- coding: utf-8 -*-
'''
structure du jeu (départ, emplacement des murs, arrivée)
'''
# General
size_sprite = 32
number_sprite_side = 15
board_size= number_sprite_side*size_sprite

title_window = "MacGyver - Labyrinthe contre Murdoc"
icon_picture = "images/macgyver.png"

name_perso = 'MacGyver'
nb_life_perso = 1

#frame per second (speed of program)
FPS = 30

# list of Images
picture_home = "images/fond.png"
picture_fond = "images/background.jpg"
picture_wall ="images/mur.jpg"

picture_start="images/macgyver_trace.png"
picture_end="images/murdoc.png"
picture_perso_right = "images/macgyver_right.png"
picture_perso_left = "images/macgyver_left.png"
picture_bad_perso = "images/murdoc.png"

picture_seringue =  "images/seringue.png"
picture_tube = "images/tube.png"
picture_ether = "images/ether.png"


#description of file for build a labyrinth
laby_file_data = "images/laby1"
char_zero = '0'
char_wall = 'm'
char_start = 'd'
char_end = 'a'
char_tools = {'seringue':'S', 'tube':'T', 'ether':'E'}

#Elements for exit
#elements = {'seringue': }
KITSURVEY = {'seringue': "images/seringue.png", \
                'tube' : "images/tube.png", \
                'ether': "images/ether.png"}
